#!/usr/bin/env python3
import numpy as np
from rplidar import RPLidar
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

PORT_NAME = '/dev/ttyUSB0'

block_distance = 500

block_angle_range = 90

lidar = RPLidar(PORT_NAME)

class jabber(Node):
	def __init__(self):
		super().__init__('path_state')
		self.publisher_ = self.create_publisher(String,'status',10)
		self.status = "free"
		self.timer = self.create_timer(0,self.pub)
	
	def pub(self):
		for scan in lidar.iter_scans():
			message = String()
			message.data = convert_message(scan)
			self.publisher_.publish(message)

def convert_message(m):
	list_of_lists = [list(i) for i in m]
	return str(np.array(list_of_lists)[:,1:3])
				
def run(args = None):
	lidar = RPLidar(PORT_NAME)
	rclpy.init(args = None)
	talker = jabber()
	rclpy.spin(talker)
	lidar.stop()
	lidar.stop_motor()
	lidar.disconnect()
	talker.destroy_node()
	rclpy.shutdown()	
	
if __name__ == '__main__':
	run()
