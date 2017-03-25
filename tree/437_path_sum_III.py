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
  
