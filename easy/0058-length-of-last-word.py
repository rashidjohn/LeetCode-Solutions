"""
Problem: 58. Length of Last Word
URL: https://leetcode.com/problems/length-of-last-word
Description: Given a string `s` consisting of words separated by spaces, return the length of the last word in the string.
Difficulty: Easy
"""

# def lengthOfLastWord(s: str) -> int:
#     return len(s.strip().split(' ')[-1])

def lengthOfLastWord(s: str) -> int:
    lenth = 0
    i = len(s) - 1
    while i >= 0 and s[i] == ' ':
        i -= 1

    while i >= 0 and s[i] != ' ':
        lenth += 1
        i -= 1
    return lenth

s = "   Hello   World    "
print(lengthOfLastWord(s))