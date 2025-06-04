# Task: Write a short Python program to count word frequencies in a text file.

# Step 1: Open the text file in read mode
with open('DailyChallenges/PythonScripts/day_7/input.txt', 'r') as file:

    text = file.read()  # Read the entire file content as a single string
# Step 2: Convert all text to lowercase to ensure case-insensitive counting
text = text.lower()
# Step 3: Remove punctuation (optional, for cleaner words)
import string
for char in string.punctuation:
    text = text.replace(char, '')
# Step 4: Split the text into individual words
words = text.split()
# Step 5: Create a dictionary to store word frequencies
word_freq = {}
# Step 6: Loop through each word and count its occurrences
for word in words:
    if word in word_freq:
        word_freq[word] += 1  # Increment count if word already in dictionary
    else:
        word_freq[word] = 1   # Initialize count to 1 if word appears first time
# Step 7: Print each word with its frequency
print("*----* Word Count *----*")
for word, count in word_freq.items():
    print(f"{word}: {count}")
