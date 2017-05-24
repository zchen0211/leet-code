'''
538. Convert BST to Greater Tree (Medium)

Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
'''

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution(object):
  def convertBST(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    stack = []
    if root is None: return None
    visited = set()
    offset = 0
    stack.append(root)

    while(len(stack)!=0):
      # record as visited and update sum = 0
      tmp = stack[-1]
      if tmp.right is not None and tmp.right not in visited: # has right and not visited, then visit it first
          stack.append(tmp.right)
      else: # unvisited rightmost
        tmp = stack.pop()
        visited.add(tmp)
        tmp.val = offset + tmp.val
        offset = tmp.val
        if tmp.left is not None:
          stack.append(tmp.left)
      for item in stack: print item.val,
      print offset


if __name__ == '__main__':
  n1 = TreeNode(2)
  n2 = TreeNode(1)
  n3 = TreeNode(13)
  n1.left, n1.right = n2, n3
  # n1.left = n2

  a = Solution()
  print a.convertBST(n1)
  print n1.val
  print n2.val
  print n3.val

