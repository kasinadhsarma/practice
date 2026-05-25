n = 5

for i in range(1, n + 1):
    # Print (n - i) * 2 spaces to align the numbers on the right
    print(" " * ((n - i) * 2), end="")
    # Print the numbers from 1 to i, separated by spaces
    for j in range(1, i + 1):
        print(j, end=" ")
    print()