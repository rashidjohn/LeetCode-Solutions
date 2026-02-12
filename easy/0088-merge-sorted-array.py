"""
Problem: 88. Merge Sorted Array
URL: https://leetcode.com/problems/merge-sorted-array/
Description: Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array. The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Difficulty: Easy
"""

def merge(nums1: list, m: int, nums2: list, n: int) -> list:
    p1, p2, i = m-1, n-1, m+n-1
    while p1>=0 and p2>=0:
        if nums1[p1] > nums2[p2]:
            nums1[i] = nums1[p1]
            p1 -= 1
        else:
            nums1[i] = nums2[p2]
            p2 -= 1
        i -= 1
    while p2 >= 0:
        nums1[i] = nums2[p2]
        p2 -= 1
        i -= 1
    return nums1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(merge(nums1, m, nums2, n))

