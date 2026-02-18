"""
Problem: 111. Minimum Depth of Binary Tree
URL: https://leetcode.com/problems/minimum-depth-of-binary-tree/
Description: Given a binary tree, find its minimum depth. The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node. Note: A leaf is a node with no children.
Difficulty: Easy
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minDepth(root: TreeNode) -> int:
    if not root:
        return 0

    left_height = minDepth(root.left)
    right_height = minDepth(root.right)

    if not root.left or not root.right:
        return max(left_height, right_height) + 1

    return min(left_height, right_height) + 1