"""
285. Inorder Successor in BST (Medium)

Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.
"""

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):
  def inorderSuccessor(self, root, p):
    """
    :type root: TreeNode
    :type p: TreeNode
    :rtype: TreeNode
    """
    # case 1: has right
    if p.right is not None:
      node = p.right
      while node.left is not None:
        node = node.left
      return node

    # step 1 locate the node
    par_map = {}
    node = root
    par_map[root] = None
    while node.val != p.val:
      if node.val > p.val:
        par_map[node.left] = node
        node = node.left
      elif node.val < p.val:
        par_map[node.right] = node
        node = node.right
      else: # find the node
        break

    # case 2: trace the node with par
    node1 = node
    while node1 is not None:
      node, node1 = node1, par_map[node1]
      if node1 is None: return None
      if node1.left == node:
        return node1
    return None

if __name__ == "__main__":
  n3 = TreeNode(3)
  n1 = TreeNode(1)
  n2 = TreeNode(2)
  n4 = TreeNode(4)
  n3.left, n3.right = n1, n4
  n1.right = n2
  # n2.left = TreeNode(1.5)

  a = Solution()
  node = a.inorderSuccessor(n3, n4)
  if node is None:
    print None
  else:
    print node.val
