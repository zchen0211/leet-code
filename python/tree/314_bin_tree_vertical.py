"""
314. Binary Tree Vertical Order Traversal (Medium)

Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples:

Given binary tree [3,9,20,null,null,15,7],
   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7
return its vertical order traversal as:
[
  [9],
  [3,15],
  [20],
  [7]
]
Given binary tree [3,9,8,4,0,1,7],
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
return its vertical order traversal as:
[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Given binary tree [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5),
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2
return its vertical order traversal as:
[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]
"""

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution(object):
  def solve2(self, root):
    cols = collections.defaultdict(list)
    queue = [(root, 0)]
    for node, i in queue:
      if node:
        cols[i].append(node.val)
        queue += (node.left, i - 1), (node.right, i + 1)
    return [cols[i] for i in sorted(cols)]


  def verticalOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    maps = {}
    q1 = [(root, 0)]

    while len(q1) != 0:
      q2 = []
      # push everything from q1 to maps
      while len(q1) != 0:
        node, idx = q1.pop()
        if idx in maps:
          maps[idx].append(node.val)
        else:
          maps[idx] = [node.val]
        if node.left is not None:
          q2.append((node.left, idx-1))
        if node.right is not None:
          q2.append((node.right, idx+1))
      q1, q2 = q2, q1
      # print maps
    ret = []
    min_, max_ = min(maps.keys()), max(maps.keys())
    for i in range(min_, max_+1):
      if i in maps:
        ret.append(maps[i])
    return ret

if __name__ == "__main__":
  n1 = TreeNode(3)
  n2 = TreeNode(9)
  n3 = TreeNode(8)
  n4 = TreeNode(4)
  n5 = TreeNode(0)
  n6 = TreeNode(1)
  n7 = TreeNode(7)
  n1.left, n1.right = n2, n3
  n2.left, n2.right = n4, n5
  n3.left, n3.right = n6, n7

  a = Solution()
  print a.verticalOrder(n1)

