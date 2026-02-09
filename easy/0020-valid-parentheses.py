"""
Problem: 20. Valid Parentheses
URL: https://leetcode.com/problems/valid-parentheses/
Description: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if:
- Open brackets must be closed by the same type of brackets.
Difficulty: Easy
"""

def isValid(s):
    stack = []
    dct = {
        '(':')',
        '{':'}',
        '[':']'
    }
    for char in s:
        if char in dct:
            stack.append(char)
        else:
            if not stack or dct[stack.pop()] != char:
                return False
    return not stack