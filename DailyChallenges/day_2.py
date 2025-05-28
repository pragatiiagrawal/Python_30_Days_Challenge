# Day 2 Python_IDC_Challenge
# Write a program that calculates the area of a rectangle using user-input length and width.

print("----Let's Calculate the area of rectangle ----")

# Step-1 Taking input from the user
# Step-2 The input function returns a string, so we use int() to convert it to an integer

length = int(input("Enter the length of the rectangle in cm: "))
width = int(input("Enter the width of the rectangle in cm: "))

# Calculating area

area = length * width
# \u00B2 is the Unicode for superscript 2 
print(f"The area of the rectangle is {area} cm\u00B2.")