#!/usr/bin/python3
'''Minimum Operations'''


def minOperations(n):
    """
        This function calculates the minimum number of operations required
        to obtain exactly n 'H' characters in this file.

        Parameters:
        n (int): The desired number of 'H' characters in the file.

        Returns:
        int: The minimum number of operations
        required to obtain n 'H' characters.
        If it is impossible to achieve n 'H' characters, return 0.
        """


pasted_chars = 1  # Initialize the number of characters in the file
clipboard = 0  # Initialize number of 'H' characters copied
counter = 0  # Initialize the operation counter

while pasted_chars < n:
    # If nothing has been copied to the clipboard yet
    if clipboard == 0:
        # Copy all characters in the file to the clipboard
        clipboard = pasted_chars
        # Increment the operation counter
        counter += 1

# If nothing has been pasted yet
if pasted_chars == 1:
    # Paste the characters in the clipboard to the file
    pasted_chars += clipboard
    # Increment the operation counter
    counter += 1
    # Continue to the next iteration of the while loop
    continue

# Calculate the number of characters that still need to be pasted
remaining = n - pasted_chars
# Check if it is impossible to achieve n characters by pasting,
# because the number of characters in the clipboard is greater than
# the remaining characters needed to reach n.
# If so, return 0 because it is impossible to achieve n.
if remaining < clipboard:
    return 0

# If the remaining number of characters cannot be evenly divided
# by the current number of characters in the file, paste the
# contents of the clipboard to add more characters.
if remaining % pasted_chars != 0:
    # Paste the contents of the clipboard to add more characters
    pasted_chars += clipboard
    # Increment the operations counter to keep track of the paste action
    counter += 1

else:
    # Copy all the characters in the file to the clipboard
    clipboard = pasted_chars
    # Paste the contents of the clipboard to double
    # the number of characters in the file
    pasted_chars += clipboard
    # Increment the operations counter twice to
    # keep track of the copy and paste actions
    counter += 2

# If the desired number of characters has been achieved,
# return the number of operations performed
if pasted_chars == n:
    return counter
# If the desired number of characters cannot be achieved, return 0
else:
    return 0
