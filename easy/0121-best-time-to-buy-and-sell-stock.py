"""
Problem: 121. Best Time to Buy and Sell Stock
URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Description: You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
Difficulty: Easy
"""

def maxProfit(prices: list[int]) -> int:
    min_price = float("inf")
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit


print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([1,2,3,4,5]))
print(maxProfit([7,6,4,3,1]))