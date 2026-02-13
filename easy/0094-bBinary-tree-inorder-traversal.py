"""
Problem: 94. Binary Tree Inorder Traversal
URL: https://leetcode.com/problems/binary-tree-inorder-traversal/
Description: Given the root of a binary tree, return the inorder traversal of its nodes' values.
Difficulty: Easy
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root: TreeNode) -> list[int]:
    res = []
    def helper(node):
        if not node:
            return
        helper(node.left)
        res.append(node.val)
        helper(node.right)
    helper(root)
    return res