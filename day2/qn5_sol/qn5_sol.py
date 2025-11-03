"""
Problem: Min-Max Finder

Write a Python program that:

1. Accepts a sequence of numbers from the user.
2. Stores the numbers in a list and finds the maximum and minimum values.
3. Stores the results (list, max, min) in a file named minmax_data.txt.
4. Reads and prints the saved data from the file.
"""

# Step 1: Accept a sequence of numbers from the user
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Step 2: Find the maximum and minimum values
max_value = max(numbers)
min_value = min(numbers)

# Step 3: Store the results in a file
with open("minmax_data.txt", "w") as file:
    file.write("Numbers List:\n")
    file.write(str(numbers) + "\n\n")
    file.write(f"Maximum Value: {max_value}\n")
    file.write(f"Minimum Value: {min_value}\n")

# Step 4: Read and print the saved data
with open("minmax_data.txt", "r") as file:
    content = file.read()

print("\nData read from file:")
print(content)
