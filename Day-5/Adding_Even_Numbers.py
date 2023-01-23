# You are going to write a program that calculates the sum of all the even numbers from 1 to 100.

# Method 1
sum_of_even=0
for number in range(1,101):
    if number%2==0:
        sum_of_even=sum_of_even+number
print(f"The sum of even number is : {sum_of_even}")

# Method 2
sum_of_even=0
for number in range(2,101,2):
    sum_of_even+=number
print(f"The sum of even number is : {sum_of_even}")