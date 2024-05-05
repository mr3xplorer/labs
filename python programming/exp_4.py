# Input a number
num = int(input("Enter a number: "))

# Print the multiplication table
print("Multiplication Table for", num)
for i in range(1, 11):
    result = num * i
    print(num, "x", i, "=", result)
