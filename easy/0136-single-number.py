"""
Problem: 136. Single Number
URL: https://leetcode.com/problems/single-number/
Description: Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. You must implement a solution with a linear runtime complexity and use only constant extra space.
Difficulty: Easy
"""

def singleNumber(nums: list[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result

print(singleNumber([2,2,1]))
print(singleNumber([4,1,2,1,2]))
print(singleNumber([1]))