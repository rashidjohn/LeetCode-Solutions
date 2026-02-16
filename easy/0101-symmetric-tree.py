"""
Problem: 101. Symmetric Tree
URL: https://leetcode.com/problems/symmetric-tree/
Description: Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
Difficulty: Easy
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root: TreeNode) -> bool:
    if not root:
        return True
    
    def mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and mirror(left.left, right.right) and mirror(left.right, right.left)
    
    return mirror(root.left, root.right)