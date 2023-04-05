#!/usr/bin/python3

def minOperations(n):
    """
    Calculates the minimum number of operations needed
    to achieve 'n' H characters in a text file.

    Args:
        n (int): the number of H characters to achieve

    Returns:
        int: the minimum number of operations needed
        to achieve 'n' H characters in a text file
    """

    # Base case: If n is 1, the file already contains
    # 1 H character, so 0 operations are needed
    if n == 1:
        return 0

    # Create an array dp to store the minimum number of operations
    # required to achieve each possible number of H characters.
    # Initialize the array with infinity for all states except the base case.
    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    # Iterate over all possible states from 2 to n
    for i in range(2, n + 1):
        # For each state, try all possible previous states j
        for j in range(1, i):
            # Check if j is a factor of i, meaning j can be combined to form i
            if i % j == 0:
                # Calculate the number of operations needed to achieve state i
                # by combining state j with (i // j) copies of state j
                operations = dp[j] + i // j
                # Update dp[i] if a smaller number of operations is found
                dp[i] = min(dp[i], operations)

                # Return the minimum number of operations required
                # to achieve the state with 'n' characters in the file
    if dp[n] == float('inf'):
        return 0
    else:
        return dp[n]
