"""
333. Largest BST Subtree (Medium)

Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.
Here's an example:
    10
    / \
   5  15
  / \   \ 
 1   8   7
The Largest BST Subtree in this case is the highlighted one. 
The return value is the subtree's size, which is 3.
Follow up:
Can you figure out ways to solve it with O(n) time complexity?
"""

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution(object):
  def largestBSTSubtree(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    self.max_ = 0
    self.helper(root)
    return self.max_

  def helper(self, node):
    # return min_, max_, num_of_nodes, True / False
    if node is None:
      return None, None, 0, True

    if node.left is None and node.right is None:
      self.max_ = max(self.max_, 1)
      return node.val, node.val, 1, True

    min_, max_ = node.val, node.val
    num = 1
    flag1, flag2 = True, True
    self.max_ = max(self.max_, num)
    if node.left is not None:
      min1_, max1_, num1, flag1 = self.helper(node.left)
      flag1 = flag1 and max1_ <= node.val
      if flag1:
        min_ = min(min_, min1_)
        num += num1

    if node.right is not None:
      min2_, max2_, num2, flag2 = self.helper(node.right)
      flag2 = flag2 and min2_ > node.val
      if flag2:
        max_ = max(max_, max2_)
        num += num2

    if flag1 and flag2:
      self.max_ = max(self.max_, num)
      return min_, max_, num, True
    else:
      return None, None, 0, False


if __name__ == "__main__":
  n1 = TreeNode(1)
  n2 = TreeNode(3)
  n3 = TreeNode(2)
  n4 = TreeNode(4)
  n5 = TreeNode(5)
  n1.left, n1.right = n2, n3
  n2.left = n4
  n3.right = n5

  a = Solution()
  print a.largestBSTSubtree(n1)
