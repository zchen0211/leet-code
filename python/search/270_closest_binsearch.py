"""
270. Closest Binary Search Tree Value (Easy)

Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:
Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        large = None
        small = None
        node = root
        while node is not None:
            if node.val == target:
                return node.val
            elif node.val > target:
                if large is None:
                    large = node.val
                large = min(large, node.val)
                node = node.left
            else:
                if small is None:
                    small = node.val
                small = max(small, node.val)
                node = node.right
        if large is None: return small
        if small is None: return large
        
        if large - target > target - small:
            return small
        else:
            return large
