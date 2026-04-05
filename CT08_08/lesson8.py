# # Lesson 8 - Vowel Counter

# ## Task 1: Open and read the file
# **Write a program that opens sherlock.txt and displays its content.​**

# Open sherlock.txt in read mode.​
# - Read the entire file content using .read().​
# - Print the content to the console.

# If the file does not exist, display an error message.

# ## Task 2: Count All Characters in the File
# **Write a program to count the total number of characters in the file, including spaces and punctuation.​**

# Open and read the file as before.​

# Use Python’s len() function to count the total number of characters in the file.​

# Print the total character count.

# ## Task 3: Identify Vowels and Count Them
# **Write a program to count how many vowels are in the file​**

# Define a set of vowels: {'a', 'e', 'i', 'o', 'u'} (case-insensitive).​

# Loop through each character in the file and check if it’s a vowel.​
# - Use a dictionary to store the count of each vowel (e.g., {'a': 500, 'e': 800}).

# Display the total vowel count.

# ## Task 4: Find the Percentage of Vowels
# **Calculate the percentage of vowels relative to the total number of characters in the file.​**

# Use the total vowel count and the total character count from previous tasks.​

# Calculate the percentage using the formula: ​
# - (total vowels / total characters) * 100.​

# Display the percentage with 2 decimal places.

# ## Task 5: Output the results into a file
# **Save the vowel counts to a new file named vowel_counts.txt.​**

# Open a new file vowel_counts.txt in write mode.​

# Write the following into the file in a clear format:​
# - counts for each vowel​
# - the percentage of vowels ​
# ​
# Confirm the file has been created successfully.

def main():
    input_path = "sherlock.txt"
    output_path = "vowel_counts.txt"
    vowels = {"a", "e", "i", "o", "u"}
    vowel_counts = {v: 0 for v in vowels}

    try:
        with open(input_path, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: '{input_path}' does not exist.")
        return

    print("--- File Content ---")
    print(content)
    print("--- End of File ---")

    total_chars = len(content)
    print(f"Total characters: {total_chars}")

    total_vowels = 0
    for char in content.lower():
        if char in vowels:
            vowel_counts[char] += 1
            total_vowels += 1

    print("Vowel counts:")
    for vowel in sorted(vowel_counts):
        print(f"{vowel}: {vowel_counts[vowel]}")

    percentage = (total_vowels / total_chars * 100) if total_chars else 0.0
    print(f"Total vowels: {total_vowels}")
    print(f"Vowels as percentage of all characters: {percentage:.2f}%")

    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write("Vowel counts in sherlock.txt\n")
        output_file.write("-----------------------------\n")
        for vowel in sorted(vowel_counts):
            output_file.write(f"{vowel}: {vowel_counts[vowel]}\n")
        output_file.write(f"\nTotal vowels: {total_vowels}\n")
        output_file.write(f"Total characters: {total_chars}\n")
        output_file.write(f"Vowels percentage: {percentage:.2f}%\n")

    print(f"Results written to '{output_path}'.")


if __name__ == "__main__":
    main()


## bonus question

