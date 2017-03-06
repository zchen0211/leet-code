import sys
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
import sys
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return sys.maxint
        min_val = sys.maxint
        if root.left is not None:
            min_val = min(min_val, root.val - root.left.val)
        if root.right is not None:
            min_val = min(min_val, root.right.val - root.val)
        result = min(min_val, self.getMinimumDifference(root.left), self.getMinimumDifference(root.right))
        print root.val, result
        return result


if __name__ == '__main__':
  node1 = TreeNode(236)
  node2 = TreeNode(104)
  node3 = TreeNode(701)
  node4 = TreeNode(227)
  node5 = TreeNode(911)

  node1.right = node3
  node3.left = node2

  sol = Solution()
  result = sol.getMinimumDifference(node1)
  print result
