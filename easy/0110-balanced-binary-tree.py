"""
Problem: 110. Balanced Binary Tree
URL: https://leetcode.com/problems/balanced-binary-tree/
Description: Given a binary tree, determine if it is height-balanced. A height-balanced binary tree is defined as a binary tree in which the difference in height between the left and right subtrees of any node is no more than one.
Difficulty: Easy
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root: TreeNode) -> bool:
    def check_height(node):
        if not node:
            return 0
        left_height = check_height(node.left)
        if left_height == -1:
            return -1
        right_height = check_height(node.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1

    return check_height(root) != -1