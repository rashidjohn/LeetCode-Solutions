"""
Problem: 13. Roman to Integer
URL: https://leetcode.com/problems/roman-to-integer/
Description: Convert a Roman numeral string to an integer value.
Difficulty: Easy
"""
def romanToInt(s):
    dct = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    total = 0
    for i in range(len(s)):
        if i+1 < len(s) and (dct[s[i]] < dct[s[i+1]]):
            total -= dct[s[i]]
        else:
            total += dct[s[i]]
    return total


n = "MCMXCIV"
print(romanToInt(n))