"""
450. Delete Node in a BST (Medium)

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
"""

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):
  def deleteNode(self, root, key):
    """
    :type root: TreeNode
    :type key: int
    :rtype: TreeNode
    """
    # step 1: find the node with the key
    node, parent = self.find(root, None, key)

    # not found
    if node is None: return root

    # node found, it has left
    if node.left is not None:
      if parent is not None:
        parent.left = node.left
      tmp = node.left
      while tmp.right is not None: tmp = tmp.right
      tmp.right = node.right
    elif node.right is not None:
      # it only has right
      if parent is not None:
        parent.left = 

    # case 1: node is a leaf node, directly delete
    if node.left is None and node.right is None:
      if parent.val > val: parent.left = None
      else: parent.right = None

  def find(self, node, parent, val):
     if node is None or node.val == val:
       return node, parent
     elif node.val > val:
       return self.find(node.left, node, val)
     else:
       return self.find(node.right, node, val)
   
  def solution2(self, root, key):
    if root is None: return None
    if root.val == key:
      # case 1: leaf
      if root.left is None and root.right is None:
        return None
      elif root.left is not None and root.right is None:
        return root.left
      elif root.right is not None and root.left is None:
        return root.right
      else: # with both left and right
        r_left = root.left
        tmp = r_left
        while tmp.right is not None: tmp = tmp.right
        tmp.right = root.right
        return r_left
    elif key < root.val:
      root.left = self.solution2(root.left, key)
    else:
      root.right = self.solution2(root.right, key)
