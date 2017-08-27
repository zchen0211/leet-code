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
