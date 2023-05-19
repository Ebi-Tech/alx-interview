#!/usr/bin/python3
"""
Main file for testing
"""


def makeChange(coins, total):
    dp = [0] + [float('inf')] * total

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
