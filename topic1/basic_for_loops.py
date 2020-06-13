"""
Program: basic_for_loops.py
Author: Daniel Meeker
Date: 06/13/2020

This program will demonstrate the use of basic for loops
"""
# Declare a list of floating point numbers
numbers = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]


# Write a for loop to print each
def print_floats():
    for i in numbers:
        print(i)


# Write a second for loop to print the odd number descending from 99 to 33 (including 99 and 33)
def print_odd():
    for i in range(99, 32, -2):
        print(i)


if __name__ == '__main__':
    print_floats()
    print_odd()
