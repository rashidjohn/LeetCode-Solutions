"""
Problem: 108. Convert Sorted Array to Binary Search Tree
URL: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
Description: Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
Difficulty: Easy
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums: list[int]) -> TreeNode:
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])
    return root