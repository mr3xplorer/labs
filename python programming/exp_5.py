
# Input the number of values to be averaged
num = int(input('How Many Numbers: '))
# Create an empty list to store the numbers
numbers = []
# Input 'n' numbers and append them to the list
for n in range(num):
    number = int(input(f'Enter number {n + 1}: '))
    numbers.append(number)

# Calculate the total sum of the numbers using the 'sum' function
total_sum = sum(numbers)
# Calculate the average by dividing the sum by 'n'
avg = total_sum / num
# Display the average
print(f'Average of {num} numbers is: {avg}')

