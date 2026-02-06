"""
Problem: 9. Palindrome Number
URL: https://leetcode.com/problems/palindrome-number
Description:
Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.
Difficulty: Easy
"""

def isPalindrome(x):
    if x < 0:
        return False
    return str(x) == str(x)[::-1]

# def isPalindrome_math(x):
#     if x < 0 or (x % 10 == 0 and x != 0):
#         return False

#     reverted_number = 0
#     while x > reverted_number:
#         reverted_number = reverted_number * 10 + x % 10
#         x //= 10

#     return x == reverted_number or x == reverted_number // 10


x = 121
print(isPalindrome(x))