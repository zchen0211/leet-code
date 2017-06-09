"""
513. Find Bottom Left Tree Value (Medium)

Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2: 
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.
"""
import collections

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):
  def findBottomLeftValue(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None: return

    queue1 = collections.deque([root])
    queue2 = []
    # BFS
    while(len(queue1) != 0):
      tmp = None
      while(queue1):
        node = queue1.popleft()
        if tmp is None: tmp = node.val
        if node.left is not None: queue2.append(node.left)
        if node.right is not None: queue2.append(node.right)
      if len(queue2) == 0: break
      else:
        queue1, queue2 = collections.deque(queue2), []
    # return result
    return tmp

if __name__ == '__main__':
  a = Solution()
  n1 = TreeNode(1)
  n2 = TreeNode(2)
  n3 = TreeNode(3)
  n4 = TreeNode(4)
  n1.left, n1.right = n2, n3
  n3.left = n4
  print a.findBottomLeftValue(n1)
