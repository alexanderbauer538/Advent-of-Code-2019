"""
Script to evaluate the first task in the Advent of Code 2019 (https://adventofcode.com) series.



Functions:
    - get_data: loads data from textfile
    - add_fuel: calculates added fuel

"""


import numpy as np
import os
import pathlib



def get_data(file_name):
    """
    Function to load the input data from a textfile.
    """
    
    input_path = pathlib.Path(os.getcwd())/'inputs'/ file_name
    loaded_data = np.loadtxt(input_path)
    
    return loaded_data

def add_fuel(input_data):
    """
    Function to calculate how much more fuel needs to be added.
    """    
    
    added_fuel = np.floor(input_data/3)-2
    
    return added_fuel

# load data
input_data = get_data('input_01.txt')

# calculations for the first part:
modules_fuel = np.sum(np.floor(input_data/3)-2)


# calculations for the second part:
total_fuel = 0

for i in range(0,len(input_data)):
    current_fuel = input_data[i]
    while (current_fuel > 6):
        new_fuel = add_fuel(current_fuel)
        total_fuel = total_fuel + new_fuel
        current_fuel = new_fuel
    

# print outputs:
print('The fuel requirement for the modules is: ',modules_fuel, 'units.')
print('The total fuel requirement is: ',total_fuel, 'units.')

