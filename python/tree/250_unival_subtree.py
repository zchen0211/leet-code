"""
250. Count Univalue Subtrees (Medium)

Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

For example:
Given binary tree,
              5
             / \
            1   5
           / \   \
          5   5   5
return 4.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.cnt = 0
        _, _ = self.helper(root)
        return self.cnt
        
    def helper(self, node):
      if node is None:
        return 0, False

      if node.left is None and node.right is None:
        self.cnt += 1
        return node.val, True

      ret_flag = True
      if node.left is not None:
        v1, flag = self.helper(node.left)
        if not flag or v1 != node.val:
          ret_flag = False

      if node.right is not None:
        v2, flag = self.helper(node.right)
        if not flag or v2 != node.val:
          ret_flag = False

      if ret_flag:
        self.cnt += 1
        return node.val, True
      else:
        return node.val, False


if __name__ == "__main__":
    n1 = TreeNode(5)
    n2 = TreeNode(1)
    n3 = TreeNode(5)
    n4 = TreeNode(5)
    n1.left, n1.right = n2, n3
    n3.right = n4
    a = Solution()
    print a.countUnivalSubtrees(n1)
