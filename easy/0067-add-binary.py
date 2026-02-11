"""
Problem: 67. Add Binary
URL: https://leetcode.com/problems/add-binary
Description: Given two binary strings a and b, return their sum as a binary string.
Difficulty: Easy
"""

def addBinary(a: str, b: str) -> str:
    result = []
    carry = 0

    m = len(a)-1
    n = len(b)-1

    while m >= 0 or n >= 0 or carry:
        digit_a = int(a[m]) if m >= 0 else 0
        digit_b = int(b[n]) if n >= 0 else 0

        total = digit_a + digit_b + carry
        result.append(str(total % 2))
        carry = total // 2

        m -= 1
        n -= 1
    return ''.join(result[::-1])

a = "11"
b = "1"
print(addBinary(a, b))

a = "1010"
b = "1011"
print(addBinary(a, b))