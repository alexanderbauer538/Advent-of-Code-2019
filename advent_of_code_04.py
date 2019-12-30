"""
Script to evaluate the fourth task in the Advent of Code 2019 (https://adventofcode.com) series.

Essentially a simple loop through the possible numberspace that checks the conditions for each number
"""



input_data = (136818,685979)

# loop for first part:
list_possible_passwords = []
cnt = 0
for i in range(136818,685979):
    if str(i) == ''.join(sorted(str(i))):
        if str(i)[0] == str(i)[1]:
            cnt = cnt+1
            list_possible_passwords.append(str(i))
        elif str(i)[1] == str(i)[2]:
            cnt = cnt+1
            list_possible_passwords.append(str(i))
        elif str(i)[2] == str(i)[3]:
            cnt = cnt+1
            list_possible_passwords.append(str(i))
        elif str(i)[3] == str(i)[4]:
            cnt = cnt+1
            list_possible_passwords.append(str(i))
        elif str(i)[4] == str(i)[5]:
            cnt = cnt+1
            list_possible_passwords.append(str(i))

print('The number of possible passwords is: ', cnt)

# loop for the second part:
list_better_passwords = []
cnt = 0        
for i in range(136818,685979):
    if str(i) == ''.join(sorted(str(i))):
        if (str(i)[0] == str(i)[1]) and ((str(i)[0] != str(i)[2])):
            cnt = cnt+1
            list_better_passwords.append(str(i))
        elif (str(i)[1] == str(i)[2]) and ((str(i)[1] != str(i)[0])) and ((str(i)[1] != str(i)[3])):
            cnt = cnt+1
            list_better_passwords.append(str(i))
        elif (str(i)[2] == str(i)[3]) and ((str(i)[2] != str(i)[1])) and ((str(i)[2] != str(i)[4])):
            cnt = cnt+1
            list_better_passwords.append(str(i))
        elif (str(i)[3] == str(i)[4]) and ((str(i)[3] != str(i)[2])) and ((str(i)[3] != str(i)[5])):
            cnt = cnt+1
            list_better_passwords.append(str(i))
        elif (str(i)[4] == str(i)[5]) and ((str(i)[4] != str(i)[3])):
            cnt = cnt+1
            list_better_passwords.append(str(i))
        
print('The number of possible passwords is: ', cnt)

