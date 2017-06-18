'''
494. Target Sum (Medium)

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.

Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
'''

class Solution(object):
  def findTargetSumWays(self, nums, S):
    """
    :type nums: List[int]
    :type S: int
    :rtype: int
    """
    rec = {0:1}
    n = len(nums)
    for i in range(n):
      item = nums[i]
      rec_ = {}
      for k in rec.keys():
        if k+item not in rec_:
          rec_[k+item] = rec[k]
        else:
          rec_[k+item] += rec[k]       
        if k-item not in rec_:
          rec_[k-item] = rec[k]
        else:
          rec_[k-item] += rec[k]
      rec = rec_
    print rec
    if S in rec: return rec[S]
    else: return 0


if __name__ == '__main__':
  a = Solution()
  print a.findTargetSumWays([1,1,1,1,1], 3)
