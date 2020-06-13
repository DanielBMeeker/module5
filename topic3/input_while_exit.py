"""
Program: input_while_exit
Author: Daniel Meeker
Date: 06/13/2020

This program will use a while loop to validate user
input and have a sentinel value to exit the loop.
It will also allow the user to exit if they have
no more input to enter.
"""
# declare a list variable
user_list = []
# declare a sentinel value for user input
sv = -99
all_done = 404
# prompt get the user input (indicating sentinel value to stop)
user_input = input("Please enter a number between 1 and 100. Enter -99 to stop. Enter 404 when finished. ")
# while sentinel value is not stopping value
while int(float(user_input)) != sv:
    # while user input is not good (in range)
    while 0 > int(float(user_input)) or int(float(user_input)) > 100:
        # Break the loop when the all done value is entered.
        if int(float(user_input)) == all_done:
            print("All Done")
            # Break out of the outer loop by changing the input to the sentinel value
            user_input = sv
            break
        # prompt user for good input
        user_input = input("Please enter a number between 1 and 100. Enter -99 to stop. Enter 404 when finished. ")
    else:
        # store in list
        user_list.append(user_input)
        # prompt and get the next user input
        user_input = input("Please enter another number between 1 and 100. Enter -99 to stop. Enter 404 when finished. ")
# print the list using a for loop
print("List of inputs: ")
for i in user_list:
    print(i)
"""
Sample input/output
Please enter a number between 1 and 100. Enter -99 to stop. Enter 404 when finished. 75
Please enter another number between 1 and 100. Enter -99 to stop. Enter 404 when finished. 404
All Done
List of inputs: 
75"""
