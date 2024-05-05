# Define a function to calculate the sum of numbers in a list
def sum_of_numbers(num_list):
    total = 0
    for num in num_list:
        total += num
    return total

# Input the number 'n'
n = int(input("Enter the number of values to sum: "))

# Initialize an empty list to store the numbers
numbers = []

# Input 'n' numbers
for i in range(n):
    num = int(input(f"Enter value {i + 1}: "))
    numbers.append(num)

# Call the function to calculate the sum
result = sum_of_numbers(numbers)

# Display the result
print(f"The sum of {n} numbers is: {result}")
