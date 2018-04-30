"""
652. Find Duplicate Subtrees (Medium)

Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1: 
        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:
      2
     /
    4
and
    4
Therefore, you need to return above trees' root in the form of a list.

"""

class TreeNode(object):
  def __init__(self, x, name=''):
    self.val = x
    self.left = None
    self.right = None
    self.name = name

class Solution(object):
  def findDup(self, root):
    self.result = []
    # traverse all_nodes
    self.table = {}

    self.inorder_(root)

    # check same sub-tree in same table
    for k in self.table.keys():
      # print 'type ', k,
      n = len(self.table[k])
      # print n
      # check if same subtree
      tmp_set = set()
      for i in range(n):
        for j in range(i+1, n):
          node1 = self.table[k][i]
          node2 = self.table[k][j]
          # print node1.val
          # print node2.val
          r = self.check_same_sub(node1, node2)
          # print node1.name, node2.name, r
          if r:
            if i not in tmp_set and j not in tmp_set:
              self.result.append(node1)
            tmp_set.add(i)
            tmp_set.add(j)
            print node1.name, node2.name
       
    return self.result

  def inorder_(self, root):
    if root is None:
      return -1
    if root.left is None and root.right is None:
      if 0 in self.table:
        self.table[0].append(root)
      else:
        self.table[0] = [root]
      return 0
    r_l = self.inorder_(root.left)
    r_r = self.inorder_(root.right)
    res = max(r_l, r_r)+1
    if res not in self.table:
      self.table[res] = [root]
    else:
      self.table[res].append(root)
    return res



  def preorder_(self, root):
    if root is None:
      return
    if root.val not in self.table:
      self.table[root.val] = [root]
    else:
      self.table[root.val].append(root)

    if root.left is not None:
      self.preorder_(root.left)
    if root.right is not None:
      self.preorder_(root.right)


  def check_same_sub(self, node1, node2):
    if node1 is None and node2 is None:
      return True
    elif node1 is None and node2 is not None:
      return False
    elif node2 is None and node1 is not None:
      return False
    elif node1.val != node2.val:
      return False

    # check subtree:
    res_l = self.check_same_sub(node1.left, node2.left)
    if res_l == False: return False
    res_r = self.check_same_sub(node1.right, node2.right)
    if res_r == False: return False

    return True


if __name__ == '__main__':
  a = TreeNode(0, 'a')
  b = TreeNode(0, 'b')
  c = TreeNode(0, 'c')
  d = TreeNode(0, 'd')
  e = TreeNode(0, 'e')
  f = TreeNode(0, 'f')
  g = TreeNode(0, 'g')
  h = TreeNode(0, 'h')
  i = TreeNode(0, 'i')

  a.left, a.right = b, c
  b.left = d
  c.right = e
  d.left, d.right = f, g
  e.left, e.right = h, i

  sol = Solution()
  print sol.check_same_sub(f, h)
  x_list = sol.findDup(a)

  for item in x_list:
    print item.val

