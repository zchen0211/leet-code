'''
199. Binary Tree Right Side View (Medium)

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
'''
import collections
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def rightSideView(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """ 
    if root is None:
      return []
    list_in = collections.deque()
    list_out = []
    list_in.append(root)
    result = []
    while(len(list_in)!=0):
      while(len(list_in)!=0):
        x = list_in.popleft()
        if len(list_in) == 0:
          result.append(x.val)
        if x.left is not None:
          list_out.append(x.left)
        if x.right is not None:
          list_out.append(x.right)
      list_in, list_out = collections.deque(list_out), list(list_in)
    return result
      
