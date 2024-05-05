# Initialize an empty list to store numbers
my_list = []

# Initialize the target number
target = int(input("Enter the number to search for: "))

# Initialize an empty list to store positions
positions = []
# Input numbers into the list
while True:
    num = int(input("Enter a number (-1 to exit): "))
    if num == -1:
        break
    my_list.append(num)

print(my_list)
# Search for the target number and record positions
position = 0
for num in my_list:
    if num == target:
        positions.append(position)
    position += 1

# Display results
if not positions:
    print("Number not found in the list.")
else:
    print("The number is found at the following positions:", positions)
