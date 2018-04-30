"""
473. Matchsticks to Square (Medium)

Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.

Example 1:
Input: [1,1,2,2,2]
Output: true

Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:
Input: [3,3,3,3,4]
Output: false

Explanation: You cannot find a way to form a square with all the matchsticks.

Note:
The length sum of the given matchsticks is in the range of 0 to 10^9.
The length of the given matchstick array will not exceed 15.
"""
import collections

class Solution(object):
  def makesquare(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    nums.sort()
    target = sum(nums)
    if target % 4 != 0: return False
    target /= 4
    n = len(nums)
    sums = [0] * 4
    return self.helper(nums, sums, target, 0)


  def helper(self, nums, sums, target, index):
    n = len(nums)
    if n == index:
      if sums[0]==target and sums[1]==target and sums[2]==target: return True
      return False
    for i in range(4):
      if nums[index]+ sums[i]>target: continue
      sums[i] += nums[index]
      if self.helper(nums, sums, target, index+1): return True
      sums[i] -= nums[index]
    return False

  def solution2(self, nums):
    def dfs(nums, pos, target):
      if pos == len(nums): return True
      for i in range(4):
        if target[i] >= nums[pos]:
          target[i] -= nums[pos]
          if dfs(nums, pos+1, target): return True
          target[i] += nums[pos]
      return False
    if len(nums) < 4: return False
    numSum = sum(nums)
    if numSum % 4 != 0: return False
    target = [numSum/4] * 4;
    return dfs(nums, 0, target)

  def solution3(self, nums):
    # AC, much faster, sorting in reverse order is very important
    def dfs(nums, pos, target):
      if pos == len(nums): return True
      for i in range(4):
        if target[i] >= nums[pos]:
          target[i] -= nums[pos]
          if dfs(nums, pos+1, target): return True
          target[i] += nums[pos]
      return False
    if len(nums) < 4 : return False
    numSum = sum(nums)
    nums.sort(reverse=True)
    if numSum % 4 != 0: return False
    target = [numSum/4] * 4;
    return dfs(nums,0, target)

if __name__ == '__main__':
  a = Solution()
  print a.makesquare([1,1,2,2,2])
  # print a.solution2([1,1,2,2,2])
  # print a.makesquare([3,3,3,3,4])
  print a.solution2([3,3,3,3,4])
  # print a.solution3([5969561,8742425,2513572,3352059,9084275,2194427,1017540,2324577,6810719,8936380,7868365,2755770,9954463,9912280,4713511])
  # print a.solution2([5969561,8742425,2513572,3352059,9084275,2194427,1017540,2324577,6810719,8936380,7868365,2755770,9954463,9912280,4713511])
  # print a.makesquare([5969561,8742425,2513572,3352059,9084275,2194427,1017540,2324577,6810719,8936380,7868365,2755770,9954463,9912280,4713511])
