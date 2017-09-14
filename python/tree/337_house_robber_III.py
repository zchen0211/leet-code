'''
337. House Robber III (Medium)
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \ 
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \ 
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.
'''

class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):
  def rob(self, root):
    res1, res2 = self.helper(root)
    return max(res1, res2, 0)

  def helper(self, root):
    # return best result both with and without root
    if root is None:
      return 0, 0
    elif root.left is None and root.right is None:
      return max(root.val, 0), 0
    else:
      # result with root
      l1, l2 = self.helper(root.left)
      r1, r2 = self.helper(root.right)
      # with root
      result1 = max(l2, 0) + max(r2, 0) + root.val
      result2 = max(l1, l2, 0) + max(r1, r2, 0)
      return result1, result2


if __name__ == '__main__':

