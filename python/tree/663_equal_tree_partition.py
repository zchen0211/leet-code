"""
663. Equal Tree Partition (Medium)

Given a binary tree with n nodes, your task is to check if it's possible to partition the tree to two trees which have the equal sum of values after removing exactly one edge on the original tree.

Example 1:
Input:     
    5
   / \
  10 10
    /  \
   2   3

Output: True
Explanation: 
    5
   / 
  10
      
Sum: 15

   10
  /  \
 2    3

Sum: 15
Example 2:
Input:     
    1
   / \
  2  10
    /  \
   2   20

Output: False
Explanation: You can't split the tree into two trees with equal sum after removing exactly one edge on the tree.
Note:
The range of tree node value is in the range of [-100000, 100000].
1 <= n <= 10000
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.stat = {}
        if root is None: return False
        tmp = self.sumdown(root)
        # print self.stat
        if tmp % 2 == 1: return False
        if tmp!=0 and tmp/2 in self.stat:
            return True
        elif tmp == 0 and self.stat[0] >= 2:
            return True
        else:
            return False
        
    def sumdown(self, node):
        s1, s2 = 0, 0
        if node.left is not None:
            s1 = self.sumdown(node.left)
        if node.right is not None:
            s2 = self.sumdown(node.right)
        result = node.val + s1 + s2
        if result not in self.stat:
            self.stat[result] = 1
        else:
            self.stat[result] += 1
        return result
