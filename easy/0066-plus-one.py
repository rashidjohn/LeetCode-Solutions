"""
Problem: 66. Plus One
URL: https://leetcode.com/problems/plus-one/
Description: Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer. The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit. You may assume the integer does not contain any leading zero, except the number 0 itself.
Difficulty: Easy
"""

def plusOne(digits: list[int]) -> list:
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits


digits = [1, 2, 3]
print(plusOne(digits))

digits1 = [9, 9, 9, 9]
print(plusOne(digits1))