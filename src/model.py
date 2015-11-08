import numpy as np
import h5py as hf
from sklearn import neighbors as skn
import sys

sys.path.append("../lib/")

import Leap
import time

class CommandModel():
	def __init__(self):
     		self.controller = Leap.Controller()				# Initialize the Leap controller
       		self.n_neighbors = 3						# Number of nearest neighbors to look at
       		self.classifier = skn.KNeighborsClassifier(self.n_neighbors)	# Model Classifier is a K neighbors algorithm
       		self.is_database_open = False					# Is a database open?

	def load_file(self, filename):
     		self.file = hf.File(filename, 'a')
       		self.commands = []
       		for group in self.file:
             		self.commands.append(group)
                self.is_database_open = True

	def close_file(self):
     		if self.is_database_open == True:
     			self.file.close()
        	else:
             		print "No database to close"
       		return

	def new_command(self, command_name):
 		if self.is_database_open == True and command_name not in self.file:
       				grp = self.file.create_group(command_name)
       				self.commands.append(command_name)
           	elif command_name in self.file:
             		print "ERROR: Command already in database"
             	else:
                  	print "ERROR: No database open"
       		return

 	def teach_command(self, command_name, data_number, data):
      		group = self.file[command_name]
      		dset = self.file[command_name].create_dataset(data_number, data=data)
		return


	def take_a_snapshot(self):
     		frame = self.controller.frame()
		data_list = []
		for hand in frame.hands:
		    	hand_x_basis = hand.basis.x_basis
		    	hand_y_basis = hand.basis.y_basis
		    	hand_z_basis = hand.basis.z_basis
		    	hand_origin = hand.palm_position
		    	hand_transform = Leap.Matrix(hand_x_basis, hand_y_basis, hand_z_basis, hand_origin)
		    	hand_transform = hand_transform.rigid_inverse()
		    	for finger in hand.fingers:
		        	transformed_position = hand_transform.transform_point(finger.tip_position)
		        	transformed_direction = hand_transform.transform_direction(finger.direction)
		        	for b in range(0, 4):
		            		bone = finger.bone(b)
		            		transformed_joint_position = hand_transform.transform_point(bone.prev_joint)
		            		transform_bone_direction = hand_transform.transform_point(bone.direction)
		            		data_list.append(transformed_joint_position[0])
		            		data_list.append(transformed_joint_position[1])
					data_list.append(transformed_joint_position[2])
					data_list.append(transform_bone_direction[0])
					data_list.append(transform_bone_direction[1])
					data_list.append(transform_bone_direction[2])
		    	data_list.append(transformed_position[0])
		    	data_list.append(transformed_position[1])
		    	data_list.append(transformed_position[2])
		    	data_list.append(transformed_direction[0])
		    	data_list.append(transformed_direction[1])
		    	data_list.append(transformed_direction[2])
		    	data_list.append(hand.palm_normal[0])
		    	data_list.append(hand.palm_normal[1])
		    	data_list.append(hand.palm_normal[2])
		    	data_list.append(hand.direction[0])
			data_list.append(hand.direction[1])
		    	data_list.append(hand.direction[2])
		data_list = np.array(data_list)
  		return data_list

	def teach_model(self):
     		data = np.zeros(131)
		return
def main():
	x = CommandModel()
 	x.load_file("new.h5")
 	print x.file["Poo!"]["1"][:]
    	x.close_file()

if __name__ == '__main__':
    main()
