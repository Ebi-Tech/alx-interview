#!/usr/bin/python3

'''Minimum Operations'''


# This function calculates the minimum number of
# operations needed to achieve 'n' H characters in a text file
def minOperations(n):
    # Base case: If n is 1, the file already contains
    # 1 H character, so 0 operations are needed
    if n == 1:
        return 0

    # Initialize the dynamic programming array 'dp'
    # with infinity for all states except the base case
    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    # Iterate over all possible states, and try to find the
    # minimum number of operations required to reach that state
    for i in range(2, n + 1):
        for j in range(1, i):
            # Check if j is a factor of i, and update
            # dp[i] if a smaller number of operations is found
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    # Return the minimum number of operations required
    # to reach the state with 'n' characters in the file
    return dp[n] if dp[n] != float('inf') else 0
