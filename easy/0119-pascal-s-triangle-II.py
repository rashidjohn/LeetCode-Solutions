"""
Problem: 119. Pascal's Triangle II
URL: https://leetcode.com/problems/pascals-triangle-ii/
Description: Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle. In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
Difficulty: Easy
"""

def getRow(rowIndex: int) -> list[int]:
    row = [1]
    for i in range(1, rowIndex+1):
        row.append(row[i-1] * (rowIndex - i + 1) // i)
    return row


print(getRow(0))
print(getRow(1))
print(getRow(2))
print(getRow(3))
print(getRow(4))
print(getRow(5))
