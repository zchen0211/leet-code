'''
312. Burst Balloons (Hard)

Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note: 
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 <= n <= 500, 0 <= nums[i] <= 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
'''

class Solution(object):
  def maxCoins(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.insert(0, 1)
    nums.append(1)
    self.table = {}
    n = len(nums)
    res = self.helper(nums, 0, n-1)
    print self.table
    return res

  def helper(self, nums, i, j):
    if (i,j) in self.table:
      return self.table[(i,j)]
    if i+1 == j:
      return 0

    res = 0
    for ii in range(i+1, j):
      tmp1 = self.helper(nums, i, ii)
      tmp2 = self.helper(nums, ii, j)
      res = max(res, tmp1+tmp2+nums[ii]*nums[i]*nums[j])
    self.table[(i,j)] = res
    return self.table[(i,j)]
       

if __name__ == "__main__":
  a = Solution()
  print a.maxCoins([3,1,5,8]) 
