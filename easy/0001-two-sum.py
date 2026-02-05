"""
Problem: Two Sum
URL: https://leetcode.com/problems/two-sum/
Description:
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
Difficulty: Easy
"""

def twoSum(nums, target):
    dct = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in dct:
            return [dct[complement], i]
        dct[num] = i


nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))