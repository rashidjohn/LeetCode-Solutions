"""
Problem 26. Remove Duplicates from Sorted Array
URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Description: Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length. Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
Difficulty: Easy
"""
def removeDuplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i+=1
            nums[i] = nums[j]
    return i+1

nums = [0,0,1,1,1,2,2,3,3,4]
length = removeDuplicates(nums)
print(length)
print(nums[:length])
print(nums)