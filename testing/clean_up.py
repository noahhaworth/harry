#!/usr/bin/env python3
import numpy as np
from adafruit_servokit import ServoKit
from time import sleep

num_of_servos = 1

delay = .003

min_imp = 500
max_imp = 2500

pca = ServoKit(channels=16)
num_of_servos = 16 #really 12, but we have 16 channels

def map(old_min,old_max,new_min,new_max,num):
	return new_min+(new_max-new_min)*(num-old_min)/(old_max-old_min)
	
time_step=.05

hip_angles = [94,84,95,90]

max_upper_angles = [75,65,75,83]#horizontal back
min_upper_angles = [2,1,165,175]#vertical down

max_lower_angles = [85,110,86,98]#red horn horizontal
min_lower_angles = [20,20,172,168]#red horn verticalish up

theta1 = np.array([])
with open('swt2.csv') as file1:
	for line in file1:
		theta1 = np.append(theta1,float(line))

theta2 = np.array([])
with open('swt3.csv') as file2:#
	for line in file2:
		theta2 = np.append(theta2,float(line))

alpha = np.append(range(100,len(theta1)),range(100))

theta1_max = np.max(theta1)
theta1_min = np.min(theta1)
theta2_max = np.max(theta2)
theta2_min = np.min(theta2)

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
		if i % 2 == 0:
			t = 100 
		pca.servo[robot.legs[i].hip_index  ].angle = hip_angles[i]
		sleep(.5)
		pca.servo[robot.legs[i].upper_index].angle = map(theta1_min,theta1_max,min_upper_angles[i],max_upper_angles[i],theta1[t])
		sleep(.5)
		pca.servo[robot.legs[i].lower_index].angle = map(theta2_min,theta2_max,min_lower_angles[i],max_lower_angles[i],theta2[t])
		sleep(.5)

class robot:
	legs = [leg(0),leg(1),leg(2),leg(3)]

def init():
	for i in range(num_of_servos):
		pca.servo[i].set_pulse_width_range(min_imp,max_imp)
#		pca.servo[robot.legs[index].lower_index].angle = new_angle
		
def main():
	victor = robot()
	init_servo_locations(victor)
	for i in range(5):
		for j in range(len(theta1)):
			for k in range(4):
				t = j		
				if k%2 == 0:
					t = alpha[t] 
				pca.servo[robot.legs[k].upper_index].angle = map(theta1_min,theta1_max,min_upper_angles[k],max_upper_angles[k],theta1[t])
				sleep(delay)
				pca.servo[robot.legs[k].lower_index].angle = map(theta2_min,theta2_max,min_lower_angles[k],max_lower_angles[k],theta2[t])
				sleep(delay)
def clean_up():
	for i in range(num_of_servos):
		pca.servo[i].angle = None
		
#sleep(3)#gives me time to run over a pull the wire if need be

if __name__ == '__main__':
#	sleep(5)#gives me time to run over and record whatever happens
	init()
#	main()
	clean_up()
