'''
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
'''

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):
  def depth(self, root):
    if not root:
      return 0
    node = root
    while(node):
      cnt += 1
      node = node.left
    return cnt

  def countNodes(self, root):
    '''
    root: TreeNode
    return int
    '''
    if root is None:
      return 0
    dleft = self.depth(root.left)
    dright = self.right(root.right)

    if dleft == dright:
      return 2**dleft + self.countNodes(root.right)
    else:
      return 2**dright + self.countNodes(root.left)
