"""
Script to evaluate the second task in the Advent of Code 2019 (https://adventofcode.com) series.



Functions:
    - get_data: loads data from textfile
    - int_computer: performs the operations (addition and multiplication) on the textfile-values

"""

import numpy as np
import os
import pathlib


def get_data(file_name):
    """
    Function to load the input data from a textfile.
    """
    
    input_path = pathlib.Path(os.getcwd())/'inputs'/ file_name
    loaded_data = np.loadtxt(input_path, delimiter=',')

    return loaded_data

def int_computer(input_array):
    """
    Function to perform the int operations and returns the processed array.
    
    Step size is 4.
    opcode 1:  add next two values
    opcode 2:  multiply next two values
    opcode 99: end codon
    """
    
    cnt = 0
    while ((input_array[cnt] != 99) and (cnt < 200) ):
    
        op_code = input_array[cnt]
        if 1 == op_code:
            input_array[input_array[cnt+3]] = input_array[input_array[cnt+1]]+input_array[input_array[cnt+2]]
            cnt = cnt+4
        
        elif 2 == op_code:
            input_array[input_array[cnt+3]] = input_array[input_array[cnt+1]]*input_array[input_array[cnt+2]]
            cnt = cnt+4
            
        else:
            print('wtf?')
            cnt = cnt+4
        
    return input_array
    

# get data and convert strings to integers
input_data = get_data('input_02.txt')
input_data = input_data.astype(int)

# change variables at beggining as per instructions
noun = 12
verb = 2
input_data[1] = noun
input_data[2] = verb

# calculations for the first part:
# create copy of list as input in function in order to retain original input data
list_for_function = input_data.copy()
output = int_computer(list_for_function)
print('The output for part one is: ',output[0])

# calculations for the second part:
# create to loops (one for the "noun" and one for the "verb") to go through all input cases
for noun in range(0,99):
    for verb in range(0,99):
        input_data[1] = noun
        input_data[2] = verb
        list_for_function = input_data.copy()
        output = int_computer(list_for_function)
        if output[0] == 19690720:
            print('The output for part two is: ',100*noun+verb)
       
   


     