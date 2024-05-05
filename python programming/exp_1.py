# Write a python program to find biggest number among four numbers using if-else

# Input four numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))

# Find the biggest number
if num1 >= num2 and num1 >= num3 and num1 >= num4:
    biggest = num1
elif num2 >= num1 and num2 >= num3 and num2 >= num4:
    biggest = num2
elif num3 >= num1 and num3 >= num2 and num3 >= num4:
    biggest = num3
else:
    biggest = num4

# Print the result
print("The biggest number is:", biggest)
