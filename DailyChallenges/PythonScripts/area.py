# Day 2 Python_IDC_Challenge
# Write a program that calculates the area of a rectangle using user-input length and width.

print("----Let's Calculate the area of rectangle ----")
# Taking input from the user
# input() returns a string, so use float() to convert it to a decimal.
length = float(input("Enter the length of the rectangle in cm: "))
width = float(input("Enter the width of the rectangle in cm: "))
# Calculating area
area = length * width
# f-string allows us to embedd expressions directly in the string.
# \u00B2 is the Unicode for superscript 2 
# .2f rounds the float to 2 decimal places.
print(f"The area of the rectangle is {area:.2f} cm\u00B2.")