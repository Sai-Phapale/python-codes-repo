n = int(input("Enter the number of elements: "))

max_number = float('-inf')  # Start with the lowest possible number

for i in range(n):
    number = float(input(f"Enter number {i + 1}: "))

    if number > max_number:
        max_number = number

print("The maximum number is:", max_number)
