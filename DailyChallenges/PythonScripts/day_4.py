while True:
    user_input = input("Enter a digit or 'exit' to quit the program.\n")
    
    if user_input =='exit'.lower():
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
