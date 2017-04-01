'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
'''

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):
  def dfs(self, root, tmp_dict, visit_arr, p, q):
    if root:
      if p in [root, root.left, root.right]:
        visit_arr[0] = True
      if q in [root, root.left, root.right]:
        visit_arr[1] = True
      if root.left:
        tmp_dict[root.left] = root
      if root.right:
        tmp_dict[root.right] = root
      if root.left and (not visit_arr[0] or not visit_arr[1]):
        self.dfs(root.left, tmp_dict, visit_arr, p, q)
      if root.right and (not visit_arr[0] or not visit_arr[1]):
        self.dfs(root.right, tmp_dict, visit_arr, p, q)


  def lCA(self, root, p, q):
    if root is None:
      return None
    elif p is None:
      return q
    elif q is None:
      return p
    tmp_dict = {}
    visit_arr = [False, False]
    self.dfs(root, tmp_dict, visit_arr, p, q)
    p_list = [p]
    while(p_list[-1] in tmp_dict):
      p_list.append(tmp_dict[p_list[-1]])
    q_list = [q]
    while(q_list[-1] in tmp_dict):
      q_list.append(tmp_dict[q_list[-1]])
    for item in p_list:
      if item in q_list:
        return item
    
