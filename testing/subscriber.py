import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import ast
import os

block_distance = 500

blocked_angle_range = 90

threashold = 0

def is_path_blocked(data):
	count = 0
	for i in range(len(data)):
		if((data[i][0]>360-blocked_angle_range/2 or data[i][0]<blocked_angle_range/2) and data[i][1] != 0 and data[i][1] < block_distance):
			count = count + 1
	if count > threashold:
		return True
	return False 
	
def clean_string(word):
	while True:
		count = 0
		first_index = word.find('[')
		second_index = word.find(']')
		third_index = word.find("  ")
		if(word[first_index+1] == ' '):
			word = word.replace("[ ",'[',1)
			count = count + 1
		if(word[second_index-1] == ' '):
			word = word.replace(" ]",']',1)
			count = count + 1
		if(word[third_index+1] == ' '):
			word = word.replace("  ",' ',1)
			count = count + 1
		if(count == 0):
			break
	return word	
		
def interp(message):
	data = []
	message = message[0:len(message)-1]
	for line in message.splitlines():
		line = line[1:len(line)]
		line = clean_string(line)
		line = line.replace(' ',',')
		data.append(ast.literal_eval(line))
	return data 

class MinimalSubscriber(Node):
	def __init__(self):
		super().__init__('listener')
		self.subscription = self.create_subscription(String,'status',self.listener_callback,10)
		self.subscription  # prevent unused variable warning
		self.publisher_ = self.create_publisher(String,'polished_status',10)
		self.green_light = True
 
	def listener_callback(self, msg):
		if(is_path_blocked(interp(msg.data))):
		#	os.system("rm check")
			self.green_light = False
		else:
		#	os.system(">check")
			self.green_light = True
		msg = String()
		msg.data = str(self.green_light)
		print(str(self.green_light))
		self.publisher_.publish(msg)
 
def main(args=None):
	rclpy.init(args=args)
	sub = MinimalSubscriber()
	rclpy.spin(sub)
	sub.destroy_node()
	rclpy.shutdown()
 
if __name__ == '__main__':
	main()
