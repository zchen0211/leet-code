"""
272. Closest Binary Search Tree Value II (Hard)

Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:
Given target value is a floating point.
You may assume k is always valid, that is: k <= total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
"""

import heapq

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution(object):
  def closestKValues(self, root, target, k):
    """
    :type root: TreeNode
    :type target: float
    :type k: int
    :rtype: List[int]
    """
    s1 = []
    s2 = []

    self.inorder(root, target, False, s1)
    print 's1', s1
    self.inorder(root, target, True, s2)
    print 's2', s2

    ret = []
    while k > 0:
      if len(s1) == 0:
        ret.append(s2.pop())
      elif len(s2) == 0:
        ret.append(s1.pop())
      elif abs(s1[-1] - target) < abs(s2[-1] - target):
        ret.append(s1.pop())
      else:
        ret.append(s2.pop())
      k -= 1
    return ret

  def inorder(self, root, target, reverse, stack):
    if root is None:
      return

    if reverse:
      self.inorder(root.right, target, reverse, stack)
    else:
      self.inorder(root.left, target, reverse, stack)

    if (reverse and root.val <= target) or (not reverse and root.val > target):
      return

    stack.append(root.val)
    if reverse:
      self.inorder(root.left, target, reverse, stack)
    else:
      self.inorder(root.right, target, reverse, stack)


if __name__ == "__main__":
  n5 = TreeNode(5)
  n2 = TreeNode(2)
  n7 = TreeNode(7)
  n5.left, n5.right = n2, n7

  a = Solution()
  ret = a.closestKValues(n5, 4, 3)
  print ret
