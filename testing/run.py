#!/usr/bin/env python3
#https://askubuntu.com/questions/1273700/enable-spi-and-i2c-on-ubuntu-20-04-raspberry-pi
import numpy as np
from adafruit_servokit import ServoKit
from time import sleep
from math import floor
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import os

STEPS_TO_TAKE = 20

WAIT = 4

trot = False

file1 = 'swt2.csv' # 'yerli1_0.txt' 'nwh1_0.csv' 'swt2.csv'

file2 = 'swt3.csv' # 'yerli2_0.txt' 'nwh2_0.csv' 'swt3.csv'

fs = 1#.5

delay = .01/2

min_imp = 500
max_imp = 2500

pca = ServoKit(channels=16)
num_of_servos = 16 #really 12, but we have 16 channels

def map(old_min,old_max,new_min,new_max,num):
	return new_min+(new_max-new_min)*(num-old_min)/(old_max-old_min)

hip_angles = [94,84,90,95]

def cut_down(data,cycle):
	trimmed = np.array([])
	for i in range(len(data)):
		if i%cycle == 0:
			trimmed = np.append(trimmed,data[i])
	return trimmed

max_upper_angles = [75,65,83,75]#horizontal back
min_upper_angles = [2,1,175,165]#vertical down

max_lower_angles = [85,110,98,40]#red horn horizontal
min_lower_angles = [20,20,168,130]#red horn verticalish up

theta1 = np.array([])
with open(file1) as file1:
	for line in file1:
		theta1 = np.append(theta1,float(line))

theta2 = np.array([])
with open(file2) as file2:
	for line in file2:
		theta2 = np.append(theta2,float(line))

#theta1 = cut_down(theta1,20)
#theta2 = cut_down(theta2,20)

theta1_avg = sum(theta1)/len(theta1)
theta2_avg = sum(theta2)/len(theta2)

theta1_max = -0
theta1_min = -90
theta2_max = -0
theta2_min = -90

#alpha_index = floor(len(theta1)/4) note that this was used for trotting with apparently good effect
alpha_25_index = floor(len(theta1)*.25)
alpha_50_index = floor(len(theta1)*.50)
alpha_75_index = floor(len(theta1)*.75)

alpha_25 = np.append(range(alpha_25_index,len(theta1)),range(alpha_25_index))
alpha_50 = np.append(range(alpha_50_index,len(theta1)),range(alpha_50_index))
alpha_75 = np.append(range(alpha_75_index,len(theta1)),range(alpha_75_index))

class leg:
	def __init__(self,index):
		self.index = index
		self.name = "leg "+str(index)
		self.hip_angle = 0
		self.upper_angle = 0
		self.lower_angle = 0
		self.hip_index = index*4
		self.upper_index = index*4+1
		self.lower_index = index*4+2
		
def init_servo_locations(robot):
	for i in range(4):
		t = 0
		if trot == True:
			if i == 1 or i == 2:
				t = alpha_50_index
		else:
			if i == 1:
				t = alpha_75_index
			elif i == 2:
				t = alpha_50_index
			else:
				t = alpha_25_index
				
		print("moving hip "+str(i)+" to "+str(hip_angles[i]))
		pca.servo[robot.legs[i].hip_index  ].angle = hip_angles[i]
		sleep(.5)
		print("moving upper "+str(i)+" to "+str(map(theta1_min,theta1_max,min_upper_angles[i],max_upper_angles[i],theta1[t])))
		pca.servo[robot.legs[i].upper_index].angle = map(theta1_min,theta1_max,min_upper_angles[i],max_upper_angles[i],theta1[t]/fs)
		sleep(.5)
		print("moving lower "+str(i)+" to "+str(map(theta2_min,theta2_max,min_lower_angles[i],max_lower_angles[i],theta2[t])))
		pca.servo[robot.legs[i].lower_index].angle = map(theta2_min,theta2_max,min_lower_angles[i],max_lower_angles[i],theta2[t]/fs)
		sleep(.5)
#		clean_up()

class robot:
	legs = [leg(0),leg(1),leg(2),leg(3)]

def init():
	for i in range(num_of_servos):
		pca.servo[i].set_pulse_width_range(min_imp,max_imp)
		
def main(args=None):
	victor = robot()
	init_servo_locations(victor)
	rclpy.init(args=args)
	sub = Subscriber()
	rclpy.spin(sub)
	sub.destroy_node()
	rclpy.shutdown()
	
def check():
	#return True
	#'''
	for file in os.listdir():
		if(file == "check"):
			print("check!!!")
			return True
	return False
#'''
class Subscriber(Node):
	def __init__(self):
		super().__init__('listener2')
		self.subscription = self.create_subscription(String,'polished_status',self.listener_callback,10)
		self.subscription  # prevent unused variable warning
		self.green_light = True
		self.timer = self.create_timer(0,self.move)
		self.global_index = 0
		self.steps_taken = 0
		 
	def listener_callback(self, msg):
		print("i heard: "+msg.data)
		self.green_light = msg.data == "True"
		
	def move(self):
		#while(self.steps_taken <= STEPS_TO_TAKE and self.green_light and check()):
		while(self.global_index <= len(theta1) and self.green_light and check() and self.steps_taken <= STEPS_TO_TAKE):
			print('running')
			for leg in range(4):
				index = self.global_index
				if trot == True:
					if leg == 1 or leg == 2:
						index = alpha_50[index]
				else:
					if leg == 1:
						index = alpha_75[index]
					elif leg == 2:
						index = alpha_50[index]
					else:
						index = alpha_25[index]
				pca.servo[robot.legs[leg].upper_index].angle = map(theta1_min,theta1_max,min_upper_angles[leg],max_upper_angles[leg],theta1[index]/fs)
				sleep(delay)
				pca.servo[robot.legs[leg].lower_index].angle = map(theta2_min,theta2_max,min_lower_angles[leg],max_lower_angles[leg],theta2[index]/fs)
				sleep(delay)
				pca.servo[robot.legs[leg].hip_index  ].angle = hip_angles[leg]
				sleep(delay)
			self.global_index = self.global_index + 1
			if(self.global_index > len(theta1)-1):
				self.global_index = 0
				self.steps_taken = self.steps_taken + 1
		if(not self.green_light):
			print('rainy day')


if __name__ == '__main__':
	sleep(WAIT)#gives me time to run over and record whatever happens
	init()
	main()
	clean_up()
