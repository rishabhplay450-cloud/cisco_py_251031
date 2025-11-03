"""
Problem 4

Write a Python program that:

1. Reads a list of names from the user (separated by spaces).
2. Sorts the names alphabetically and stores them in a list.
3. Converts the list into a tuple.
4. Saves the sorted list and tuple into a file named names_data.txt.
5. Reads and prints the saved data from the file.
"""

# Step 1: Read names from the user
names = input("Enter names separated by spaces: ").split()

# Step 2: Sort names alphabetically
sorted_names = sorted(names)

# Step 3: Convert the list into a tuple
names_tuple = tuple(sorted_names)

# Step 4: Save the list and tuple into a file
with open("names_data.txt", "w") as file:
    file.write("Sorted Names List:\n")
    file.write(str(sorted_names) + "\n\n")
    file.write("Names Tuple:\n")
    file.write(str(names_tuple) + "\n")

# Step 5: Read and display the data from the file
with open("names_data.txt", "r") as file:
    content = file.read()

print("\nData read from file:")
print(content)
