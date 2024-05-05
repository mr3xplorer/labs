m = int(input("Enter starting number: ")) #22
n = int(input("Enter ending number: ")) #5

if m >= n:
    print("starting number should be less than ending number.")
else:
    for i in range(m, n):
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            print(i)

            