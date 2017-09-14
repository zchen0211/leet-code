"""
508. Most Frequent Subtree Sum (Medium)

Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.
Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.

Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.
"""

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):
  def findFrequentTreeSum(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root is None: return []
    stat = {}
    _ = self.helper(root, stat)
    print stat 
    max_ = max(stat.values())
    result = [item for item in stat if stat[item]==max_]
    return result

  def helper(self, node, stat):
    # return sum of the subtree
    # update stat
    if node.left is None and node.right is None:
      if node.val in stat: stat[node.val] += 1
      else: stat[node.val] = 1
      return node.val
    else:
      if node.left is not None:
        l_ = self.helper(node.left, stat)
      else: l_ = 0
      if node.right is not None:
        r_ = self.helper(node.right, stat)
      else: r_ = 0
      tmp_sum = node.val + l_ + r_
      if tmp_sum in stat: stat[tmp_sum] += 1
      else: stat[tmp_sum] = 1
      return tmp_sum

if __name__ == '__main__':
  n1 = TreeNode(1)
  n2 = TreeNode(0)
  n3 = TreeNode(-1)
  n1.left, n1.right = n2, n3
  a = Solution()
  print a.findFrequentTreeSum(n1)
