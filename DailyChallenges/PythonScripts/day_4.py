# Day 4 
# Challenge: Write a program to check if a user-entered number is prime.
# Prime Number: A number is a prime number if it is divisible by 1 and the number itself.

while True:
    user_input = input("Enter a digit or 'Exit' to quit the program.\n")
    
    if user_input.lower() == 'exit':
        print("--- Exiting the Program ----")
        break
    if not user_input.isdigit():
        print("Invalid number! Please enter a valit number. ")
        print("--------------------------------------------------")
        continue
    num = int(user_input)
    count = 0
    for i in range (1,num+1):
        if num % i == 0:
            count +=1
            if count > 2:
                break
    if count == 2:
        print("This is  a prime number.")
        print("--------------------------------------------------")
    else:
        print("This is not a prime number")
        print("--------------------------------------------------")
