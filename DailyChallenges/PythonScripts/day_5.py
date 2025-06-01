# Write a function that calculates the sum and average of a list of numbers

num_list = [15,42,55,75,80,92,100] 
def cal_sum_and_average():
    total = 0
    for num in num_list:
       total+=num
    average = total/len(num_list)
    return total,average
total,average = cal_sum_and_average()
print(f"The sum of numbers is {total}")
print(f"The average of numbers is {average:.2f}")


