"""
Program: while_loop_input_validation
Author: Daniel Meeker
Date: 06/13/2020

This program will use a while loop to validate user
input and have a sentinel value to exit the loop.
"""
# declare a list variable
user_list = []
# declare a sentinel value for user input
sv = -99
# prompt get the user input (indicating sentinel value to stop)
user_input = input("Please enter a number between 1 and 100. Enter -99 to stop. ")
# while sentinel value is not stopping value
while int(float(user_input)) != sv:
    # while user input is not good (in range)
    if 0 > int(float(user_input)) or int(float(user_input)) > 100:
        # prompt user for good input
        user_input = input("Please enter a number between 1 and 100. Enter -99 to stop. ")
    else:
        # store in list
        user_list.append(user_input)
        # prompt and get the next user input
        user_input = input("Please enter another number between 1 and 100. Enter -99 to stop. ")
# print the list using a for loop
print("List of inputs: ")
for i in user_list:
    print(i)
"""
Sample input/output
Please enter a number between 1 and 100. Enter -99 to stop. 333
Please enter a number between 1 and 100. Enter -99 to stop. 75
Please enter another number between 1 and 100. Enter -99 to stop. 95
Please enter another number between 1 and 100. Enter -99 to stop. 45
Please enter another number between 1 and 100. Enter -99 to stop. 33
Please enter another number between 1 and 100. Enter -99 to stop. -99
List of inputs: 
75
95
45
33
"""
