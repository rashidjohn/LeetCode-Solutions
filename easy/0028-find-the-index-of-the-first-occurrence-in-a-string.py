"""
Problem: 28. Find the Index of the First Occurrence in a String
URL: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
Description: Given two strings `haystack` and `needle`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.
Difficulty: Easy
"""

def strStr(haystack: str, needle: str) -> int:
    if not needle:
        return 0

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i

    return -1


matn = "sadbutsad"
needle = "sad"
print(strStr(matn, needle))