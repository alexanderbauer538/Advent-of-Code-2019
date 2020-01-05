"""
Script to evaluate the sixth task in the Advent of Code 2019 (https://adventofcode.com) series.

Functions:
    - get_data: loads data from textfile
    - path_to_center: get list of orbits from one object to the center of mass
"""




import os
import pathlib


def get_data(file_name):
    """
    Function to load the input data from a textfile.
    """
   
    input_path = pathlib.Path(os.getcwd())/'inputs'/ file_name
    file_to_read = open(input_path, 'r')
    output_data = file_to_read.readlines()
    file_to_read.close()
    return output_data

def path_to_center(start_point):
    """
    Function to create a list that denotes the path from one starting orbit to the center of mass (COM).
    """
    
    path_to_find = []
    current_position = start_point
    while current_position != 'COM':
        new_index = objects.index(current_position)
        current_position = coms[new_index]
        print(current_position)
        path_to_find.append(current_position)
        
    return path_to_find
    
# load data from file
input_data = get_data('input_06.txt')
input_data = [w.strip() for w in  input_data]

# split input data into objects and orbits
coms = [i.split(')', 1)[0] for i in input_data]
objects = [i.split(')', 1)[1] for i in input_data]

# loop from every object towards the center of mass 'COM' and count the total orbits in checksum
checksum = 0
for i in range(0,len(objects)):
    current_position = objects[i]
    while current_position != 'COM':
        new_index = objects.index(current_position)
        current_position = coms[new_index]
        checksum = checksum+1

print('The total number of orbits in the system is: ',checksum)
     
santas_path = path_to_center('SAN')
my_path = path_to_center('YOU')

while santas_path[-1] == my_path[-1]:
    del santas_path[-1]
    del my_path[-1]

orbits_to_traverse = len(santas_path)+len(my_path)

print('The number of orbits to traverse is: ',orbits_to_traverse)



