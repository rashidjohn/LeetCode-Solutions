"""
Problem: 112. Path Sum
URL: https://leetcode.com/problems/path-sum/
Description: Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum. A leaf is a node with no children.
Difficulty: Easy
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root: TreeNode, tagetSum: int) -> bool:
    if not root:
        return False
    
    targetSum -= root.val

    if not root.left and not root.right:
        return targetSum == 0
    
    return hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum)