"""
666. Path Sum IV (Medium)

If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digits integers.

For each integer in this list:
 1. The hundreds digit represents the depth D of this node, 1 <= D <= 4.
 2. The tens digit represents the position P of this node in the level it belongs to, 1 <= P <= 8. The position is the same as that in a full binary tree.
 3. The units digit represents the value V of this node, 0 <= V <= 9.
Given a list of ascending three-digits integers representing a binary with the depth smaller than 5. You need to return the sum of all paths from the root towards the leaves.

Example 1:
Input: [113, 215, 221]
Output: 12
Explanation: 
The tree that the list represents is:
    3
   / \
  5   1

The path sum is (3 + 5) + (3 + 1) = 12.

Example 2:
Input: [113, 221]
Output: 4
Explanation: 
The tree that the list represents is: 
    3
     \
      1

The path sum is (3 + 1) = 4.
"""

class TreeNode(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

class Solution(object):
  def pathSum(self, nums):
    n = len(nums)
    if n == 0: return 0

    stat = {}
    for item in nums:
      # parse item
      d = item / 100
      l = (item / 10) % 10
      v = item % 10
      print d,l,v
      stat[(d,l)] = (v, 1)
      if l%2==0 and (d,l-1) in stat:
        d_, l_ = d-1, (l+1)/2
        while d_ != 0:
          v, c = stat[(d_,l_)]
          stat[(d_,l_)] = (v, c+1)
          d_, l_ = d_-1, (l_+1)/2
    result = 0
    for k in stat.keys():
      v, c = stat[k]
      result += v*c
    return result


if __name__ == "__main__":
  a = Solution()
  print a.pathSum([113,215,221])
  print a.pathSum([113,221])
