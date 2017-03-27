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
