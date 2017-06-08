'''
404. Sum of Left Leaves (Easy)

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
Subscribe to see which companies asked this question.
'''

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):
  def sumOfLeftLeaves(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
      return 0
    elif root.left is None and root.right is None:
      return 0

    if root.left is not None: #
      cnt = 0
      if root.left.left is None and root.left.right is None:
        cnt += root.left.val
      cnt += self.sumOfLeftLeaves(root.left)
    
    if root.right is not None:
      cnt += self.sumOfLeftLeaves(root.right)
    return cnt


if __name__ == '__main__':
  node1 = TreeNode(3)
  node2 = TreeNode(9)
  node3 = TreeNode(20)
  node4 = TreeNode(15)
  node5 = TreeNode(7)
  node1.left = node2
  node1.right = node3
  node3.left = node4
  node3.right = node5

  a = Solution()
  print a.sumOfLeftLeaves(node1)
