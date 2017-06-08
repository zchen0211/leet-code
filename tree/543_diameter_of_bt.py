'''
543. Diameter of Binary Tree (Easy)

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
'''

# Definition for a binary tree node.
class TreeNode(object):  
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):
  def diameter(self, root):
    _, res = self.helper_func(root)
    return max(0,res-1)
  def helper_func(self, root):
    # return self_depth_right, best result
    if root == None:
      return 0, 0
    else:
      l_depth, l_best_res = self.helper_func(root.left)
      r_depth, r_best_res = self.helper_func(root.right)
      return max(l_depth, r_depth)+1, max(l_best_res, r_best_res, l_depth+r_depth+1)

    
if __name__ == '__main__':
  node1 = TreeNode(1)
  node2 = TreeNode(2)
  node3 = TreeNode(3)
  node4 = TreeNode(4)
  node5 = TreeNode(5)
  node1.left = node2
  node1.right = node3
  node2.left = node4
  node2.right = node5
  
  a = Solution()
  print a.diameter(node1)
