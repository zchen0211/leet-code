"""
689. Maximum Sum of 3 Non-Overlapping Subarrays (Hard)

In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

Example:
Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
Note:
nums.length will be between 1 and 20000.
nums[i] will be between 1 and 65535.
k will be between 1 and floor(nums.length / 3).
"""

class Solution(object):
  def maxSumOfThreeSubarrays(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    # step 1: get the sums
    sums_ = [0]
    for item in nums:
      sums_.append(sums_[-1] + item)

    n = len(nums)
    sums = []
    for i in range(n-k+1):
      sums.append(sums_[i+k] - sums_[i])
    print sums

    # dp
    print len(sums), n-k+1
    res1 = [0] * (n-k+1)
    res2 = [None] * (n-k+1)
    res3 = [None] * (n-k+1) 

    res1_ = [0] * (n-k+1)
    res2_ = [0] * (n-k+1)
    res3_ = [0] * (n-k+1)
    res1_[0] = sums[0]
 
    for i in range(1, n-k+1):
      if sums[i] > res1_[i-1]:
        res1[i] = i
        res1_[i] = sums[i]
      else:
        res1[i] = res1[i-1]
        res1_[i] = res1_[i-1]

      if i >= k: # can produce new
        result = sums[i] + res1_[i-k]
        print result
        if res2[i-1] is None:
          res2[i] = (res1[i-k], i)
          res2_[i] = result
        else: 
          if result > res2_[i-1]:
            res2[i] = (res1[i-k], i)
            res2_[i] = result
          else:
            res2[i] = res2[i-1]
            res2_[i] = res2_[i-1]

      if i >= 2*k:
        result = sums[i] + res2_[i-k]
        if res3[i-1] is None:
          res3[i] = (res2[i-k][0], res2[i-k][1], i)
          res3_[i] = result
        else: 
          if result > res3_[i-1]:
            res3[i] = (res2[i-k][0], res2[i-k][1], i)
            res3_[i] = result
          else:
            res3[i] = res3[i-1]
            res3_[i] = res3_[i-1]
      print 'step :', i
      print res1, res2, res3
      print res1_, res2_, res3_

if __name__ == "__main__":
  a = Solution()
  # print a.maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2)
  # print a.maxSumOfThreeSubarrays([17,7,19,11,1,19,17,6,13,18,2,7,12,16,16,18,9,3,19,5], 6)
  # print a.maxSumOfThreeSubarrays([17,8,14,11,13,9,4,19,20,6,1,20,6,5,19,8,5,16,20,17], 5)
  nums = [7,15,9,13,19,1,17,16,15,11,19,14,7,5,11,10,5,16,16,2,16,18,2,17,15,9,9,6,15,19,13,9,13,15,1,11,13,17,8,16]
  k = 10
  print a.maxSumOfThreeSubarrays(nums, k)
