"""
Problem: 27. Remove Element
URL: https://leetcode.com/problems/remove-element/
Description: Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
- Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
- Return k.
Difficulty: Easy
"""

def removeElement(nums, val):
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i+=1
    return i

nums = [3,2,2,3]
val = 3
length = removeElement(nums, val)
print(length)
print(nums[:length])
print(nums)