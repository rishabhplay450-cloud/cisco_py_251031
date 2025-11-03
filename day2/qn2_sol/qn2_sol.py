"""
This program:
1. Reads a line of integers from the user (separated by spaces).
2. Stores them in a list.
3. Calculates and displays the sum and average.
"""

# Step 1: Read integers from user input
numbers = list(map(int, input("Enter integers separated by spaces: ").split()))

# Step 2: Calculate sum and average
total = sum(numbers)
average = total / len(numbers) if numbers else 0
print(f"Sum: {total}")
print(f"Average: {average}")    
print("to/from file.......")
# Store results in a file

# Step 3: Save data to a text file
with open("qn02_data.txt", "w") as output_file:
    output_file.write(f"List: {numbers}\n")
    output_file.write(f'Sum: {total}\n')
    output_file.write(f'Average: {average}\n')

# Step 4: Read and display data from the file
with open("qn02_data.txt", "r") as input_file:
    contents1 = input_file.read()
    contents2 = input_file.read()
    contents3 = input_file.read()
    print("Contents of qn02_data.txt:")
    print(contents1)
    print(contents2)    
    print(contents3)   
