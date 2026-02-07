"""
Problem: 14. Longest Common Prefix
URL: https://leetcode.com/problems/longest-common-prefix
Description: Find the longest common prefix string among an array of strings. If there is no common prefix, return an empty string "".
Difficulty: Easy
"""

def longestCommonPrefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for string in strs[1:]:
        while string.find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
    
strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))