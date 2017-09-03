"""
669. Trim a Binary Search Tree (Easy)

Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.

Example 1:
Input: 
    1
   / \
  0   2

  L = 1
  R = 2

Output: 
    1
      \
       2
Example 2:
Input: 
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output: 
      3
     / 
   2   
  /
 1
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        node = self.remove_left(root, L)
        node = self.remove_right(node, R)
        return node
        
    def remove_left(self, root, L):
        if root is None:
            return None
        if root.val >= L:
            root.left = self.remove_left(root.left, L)
            return root
        elif root.val < L:
            print 'here'
            if root.right is not None:
                node = self.remove_left(root.right, L)
                print node.val
                return node
            else:
                return None
            
    def remove_right(self, root, R):
        if root is None:
            return None
        if root.val <= R:
            print 'there'
            root.right = self.remove_right(root.right, R)
            return root
        elif root.val > R:
            if root.left is not None:
                return self.remove_right(root.left, R)
            else:
                return None


if __name__ == "__main__":
  n1 = TreeNode(1)
  # n2 = TreeNode(0)
  n3 = TreeNode(2)
  # n1.left = n2
  n1.right = n3

  a = Solution()
  result = a.trimBST(n1, 2, 4)
  print result.val
  print result.left, result.right
