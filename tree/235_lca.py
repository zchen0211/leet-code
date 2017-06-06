'''
235. Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
'''

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution(object):
  def helper_traverse(self, root, parent_map):
    if root is None:
      return
    else:
      if root.left is not None:
        parent_map[root.left] = root
        self.helper_traverse(root.left, parent_map)
      if root.right is not None:
        parent_map[root.right] = root
        self.helper_traverse(root.right, parent_map)
    return


  def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    parent_map = {}
    self.helper_traverse(root, parent_map)
    p_parent = [p]
    q_parent = [q]
    tmp_n = p
    while(parent_map.has_key(tmp_n)):
      p_parent.append(parent_map[tmp_n])
      tmp_n = parent_map[tmp_n]

    tmp_n = q
    while(parent_map.has_key(tmp_n)):
      p_parent.append(parent_map[tmp_n])
      tmp_n = parent_map[tmp_n]

    for tmp_n in p_parent:
      if tmp_n in q_parent:
        return tmp_n.val
