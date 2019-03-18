"""
572 Subtree of Another Tree (Easy)

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if t is None:
            return s is None
        if s is None:
            return t is None
        if s.val == t.val:
            if self.helper(s, t):
                return True
        if self.isSubtree(s.left, t):
            return True
        if self.isSubtree(s.right, t):
            return True
        return False

    def helper(self, s, t):
        # return if s and t are exactly the same
        if s is None:
            return t is None
        if t is None:
            return s is None
        if s.val != t.val:
            return False
        else:
            if self.helper(s.left, t.left) and self.helper(s.right, t.right):
                return True
        return False
