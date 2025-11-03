"""
Problem 3

    Write a Python program that:

    1. Accepts a sentence from the user.
    2. Splits the sentence into words and stores them in a **list**.
    3. Converts all words to **uppercase** and stores them in a **tuple**.
    4. Saves both the list and tuple into a file named **`sentence_data.txt`**.
    5. Reads back the data from the file and displays it on the scre
"""

# Step 1: Accept a sentence from the user
sentence = input("Enter a sentence: ")

# Step 2: Split the sentence into words and store them in a list
words_list = sentence.split()

# Step 3: Convert all words to uppercase and store them in a tuple
uppercase_tuple = tuple(word.upper() for word in words_list)

# Step 4: Save both the list and tuple into a file
with open("sentence_data.txt", "w") as file:
    file.write("Words List:\n")
    file.write(str(words_list) + "\n\n")
    file.write("Uppercase Tuple:\n")
    file.write(str(uppercase_tuple) + "\n")

# Step 5: Read back the data from the file and display it
with open("sentence_data.txt", "r") as file:
    content = file.read()

print("\nData read from file:")
print(content)
