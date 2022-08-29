# Title: wolff_calculator.py
# Author: Patrick Wolff
# Date: 08 August 2022
# Description: Python program to test using variables and functions

# Add function
def add (x, y):
    return x + y

# Subtract function 
def subtract (x, y):
    return x - y

# Divide function
def divide (x, y):
    return x / y

# Multiply function
def multiply (x, y):
    return x * y

# Variables to test functions
num1 = 4
num2 = 10
num3 = 6
num4 = 8
num5 = 2

#Variable to hold values from above methods
add_total = add(num1, num1)
sub_total = subtract(num2, num3)
div_total = divide(num4, num5)
multiply_total = multiply(num2, num5)

#Variables to hold strings to show results
output_add = "4 + 4 is {0}".format(add_total)
output_subtract = "10 - 6 is {0}".format(sub_total)
output_divide = "8 / 2 is {0}".format(div_total)
output_multiply = "10 * 2 is {0}".format(multiply_total)

print(output_add)
print(output_subtract)
print(output_divide)
print(output_multiply)