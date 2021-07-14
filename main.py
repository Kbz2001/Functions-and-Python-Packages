# Warm Up
#--------

# Use nested for loops to recreate the output below:
# print(1)
# print(1, 2)
# print(1, 2, 3)
# print(1, 2, 3, 4)
# print(1, 2, 3, 4, 5)

# New lines: "\n", print()
# for i in range(1, 6):
#   for j in range(0, i):
#     print(j + 1, end=" ")
#   print()

# Write a Python program to test if a number is positive or negative. The program will ask the user to input a number, then it will display what the number is.
# number = input("Type a random number: ")
# number = int(number)
# if number > 0:
#   print("Number is greater than 0 (positive)")
# elif number < 0:
#   print("Number is less than 0 (negative)")
# else:
#   print("Number is 0")

# Functions
#----------
# Math Definition: inputs provide outputs
# Programming Definition: functions take in inputs (parameters) and return values 

# Why do we use functions?
# Break up code into managable chunks.
# The ability to reuse code rather than copy pasting it.
# Makes the code more organized.

# No value returned == Void function
# This is a void function
# def HelloWorld():
#   print("Hello World!")

# # Calling a function
# HelloWorld()

# With parameters (My parameter is name)
# This is a void function
# def greeting(name):
#   print("Hello " + name)

# myName = input("What is your name? ")
# greeting(myName)

# Return function (A function that returns a value)
# Return statements are always the last thing in the function. Functions stop running once it reaches a return statement.

# def addNumbers(inputNumber, inputNumber2):
#   output = int(inputNumber) + int(inputNumber2)
#   return output

# inputNumber1 = input("Enter the first number: ")
# inputNumber2 = input("Enter the second number: ")

# print(addNumbers(inputNumber1, inputNumber2))

# Function Practice
#------------------
# Create a function that can multiply two numbers

# Python Packages
# Python comes with libaries. Libraries/Packages in Python contain useful functions that we can use to make writing code easier for us.
# Ex. random, turtle, example games
# To use a library in Python we call the import statement
# Ex. import random
# Ex. import turtle
# If you don't know the name of the function to call in the library look at the documentation.
import turtle
# Drawing a square
Z = turtle.Turtle()
# Forward/Backward units of measurement is pixels
Z.forward(50)
# for Left/Right movement units of measurment is degrees(angle)
Z.left(90)
Z.forward(50)
Z.right(90)
Z.backward(50)
Z.right(90)
Z.forward(50)
Z.speed(1)

# Drawing a equilateral triangle
triangle = turtle.Turtle()
triangle.speed(1)
triangle.forward(100)
triangle.left(120)
triangle.forward(100)
triangle.left(120)
triangle.forward(100)
# Reminder: 10-15 min break