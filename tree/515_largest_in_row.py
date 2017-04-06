'''
You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]
'''

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):
  def largestValues(self, root):
    if root is None:
      return []
    result = []
    tmp_result = [] 
    stack1 = [root]
    stack2 = []

    while(stack1):
      # visit everything in stack1, if has children, push to stack2
      while(stack1):
        tmp_node = stack1.pop()
        tmp_result.append(tmp_node.val)
        if tmp_node.left:
          stack2.append(tmp_node.left)
        if tmp_node.right:
          stack2.append(tmp_node.right)
      # push values into tmp_result,
      # append max of tmp_result to result
      result.append(max(tmp_result))
      # swap stack2, stack1; clean tmp_result
      tmp_result = []
      stack1, stack2 = stack2, stack1
    return result


if __name__ == '__main__':
  node1 = TreeNode(1)
  node2 = TreeNode(3)
  node3 = TreeNode(2)
  node4 = TreeNode(5)
  node5 = TreeNode(3)
  node6 = TreeNode(9)
  node1.left, node1.right = node2, node3
  node2.left, node2.right = node4, node5
  node3.right = node6
  a = Solution()
  print a.largestValues(node1)
