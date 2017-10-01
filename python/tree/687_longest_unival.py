"""
687. Longest Univalue Path (Easy)

Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

2
Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res1, res2 = self.helper(root)
        return res2 - 1
        
    def helper(self, root):
        # return [0]: longest path with same val
        # return [1]: best value with this as root
        if root is None:
            return 0, 0
        
        # longest path l
        if root.left is not None and root.left.val == root.val:
            long_pathl = self.helper_path(root.left)
        else:
            long_pathl = 0
        # longest path r
        if root.right is not None and root.right.val == root.val:
            long_pathr = self.helper_path(root.right)
        else:
            long_pathr = 0
        # 1 + l + r
        res = 1 + long_pathl + long_pathr
        # max(1+l, 1+r)
        long_path = 1 + max(long_pathl, long_pathr)
        _, res2 = self.helper(root.left)
        _, res3 = self.helper(root.right)
        print 'root:', root.val, res, res2, res3
        return long_path, max(res, res2, res3)
        
    def helper_path(self, root):
        if root is None: return 0
        path_l, path_r = 1, 1
        if root.left is not None and root.left.val == root.val:
            path_l += self.helper_path(root.left)
        if root.right is not None and root.right.val == root.val:
            path_r += self.helper_path(root.right)
        return max(path_l, path_r)


if __name__ == "__main__":
  n1 = TreeNode(1)
  n2 = TreeNode(4)
  n3 = TreeNode(5)
  n4 = TreeNode(4)
  n5 = TreeNode(4)
  n6 = TreeNode(5)
  n1.left, n1.right = n2, n3
  n2.left, n2.right = n4, n5
  n3.right = n6

  a = Solution()
  print a.helper_path(n1)
  print a.longestUnivaluePath(n2)
