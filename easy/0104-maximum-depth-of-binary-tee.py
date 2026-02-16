"""
Problem: 104. Maximum Depth of Binary Tree
URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/
Description: Given the root of a binary tree, return its maximum depth. The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node.
Difficulty: Easy
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0

    left_height = maxDepth(root.left)
    right_height = maxDepth(root.right)
    return max(left_height, right_height) + 1