"""
Problem: 118. Pascal's Triangle
URL: https://leetcode.com/problems/pascals-triangle/
Description: Given an integer numRows, return the first numRows of Pascal's triangle. In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
Difficulty: Easy
"""

def generate(numRows: int) -> list[list[int]]:
    if numRows == 0:
        return []
    
    triangle = [[1]]

    for i in range(1, numRows):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle