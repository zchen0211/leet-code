'''
213. House Robber II (Medium)

Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

'''

class Solution(object):
  def rob(self, nums):
    if not nums:
      return 0
    if len(nums) == 1:
      return nums[0]
    elif len(nums) in [2,3]:
      return max(nums)

    b1 = nums[0] # with current, with 0
    b2 = -1 # without current, with 0
    b3 = -1 # with current, without 0
    b4 = 0 # without current, without 0
    
    n = len(nums)
    for i in range(1, n):
      if i == 1:
        b1, b2, b3, b4 = 0, nums[0], nums[1], 0
      elif i == 2:
        b1, b2, b3, b4 = b2+nums[i], b2, nums[2], nums[1] 
      elif i!=n-1:
        b1, b2, b3, b4 = b2+nums[i], max(b1,b2), b4+nums[i], max(b3,b4)
      else: # i==n-1
        b1, b2, b3, b4 = 0, max(b1,b2), b4+nums[i], max(b3,b4)
    return max(b1,b2,b3,b4)

  def solve2(self, nums):
    # AC, best understanding, slightly slower
    n = len(nums)
    if n==0: return 0
    if n==1: return nums[0]
    return max(self.helper(nums[:-1]), self.helper(nums[1:]))

  def helper(self, nums):
    n = len(nums)
    best_w = nums[0]
    best_wo = 0
    for i in range(1, n):
      best_w, best_wo = best_wo + nums[i], max(best_w, best_wo)
    return max(best_w, best_wo)
           
