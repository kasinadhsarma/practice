n = 5

for i in range(1, n + 1):
    # Print leading spaces to center the triangle
    print(" " * (n - i), end="")
    # Print numbers from 1 to i, separated by spaces
    for j in range(1, i + 1):
        print(j, end=" ")
    print()