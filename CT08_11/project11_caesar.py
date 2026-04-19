# Lesson 11 - Caesar Encryption

## Task 1: Encrypt/ Decrypt a single character

### Create a function to encrypt/ decrypt a single character
# `caesar_shift_character ()`
# - **Arguments**: 
#   - **char (str)**: A single character to shift.
#   - **key (int)**: The encryption/decryption key (shift value).
#   - **mode (str)**: "encrypt" or "decrypt" to specify the operation.
# - **Return Value**:
#   - **str**: The shifted character, or the original character if it’s outside the printable ASCII range.

# ### Notes
# *This is the hardest function as it handles the encryption/ decryption at the character level.*

# *Take some time to understand the math and algorithm in the previous slides!*

# *Ask your Code Mentor to explain to you!*
# 1. change your character to ascii.
# 2. minus the ascii by 32
# 3. shift the key (meaning add/substract) by number
#