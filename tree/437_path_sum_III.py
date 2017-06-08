'''
437 Path Sum III (Easy)

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
'''

class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution(object):
  def HelperFunc(self, root, target):
    if root:
      cnt = 0
      if root.val == target:
        cnt += 1
      if root.left:
        cnt += self.HelperFunc(root.left, target-root.val)
      if root.right:
        cnt += self.HelperFunc(root.right, target-root.val)
      return cnt
    else:
      return 0

  def pathSum(self, root, target):
    cnt = 0
    if root:
      cnt += self.HelperFunc(root, target)
    if root.left:
      cnt += self.pathSum(root.left, target)
    if root.right:
      cnt += self.pathSum(root.right, target)
    return cnt

if __name__ == '__main__':
  # node1 = TreeNode(1)
  # node2 = TreeNode(1)
  # node1.left = node2  
  
  node1 = TreeNode(10)
  node2 = TreeNode(5)
  node3 = TreeNode(-3)
  node4 = TreeNode(3)
  node5 = TreeNode(2)
  node6 = TreeNode(11)
  node7 = TreeNode(3)
  node8 = TreeNode(-2)
  node9 = TreeNode(1)
  
  node1.left = node2
  node1.right = node3
  node2.left = node4
  node2.right = node5
  node3.right = node6
  node4.left = node7
  node4.right = node8
  node5.right = node9
  a = Solution()
  print a.pathSum(node1, 8)
  
