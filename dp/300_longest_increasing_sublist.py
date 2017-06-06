'''
300. Longest Increasing Subsequence (Medium)

Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
'''

class Solution(object):
  def lengthOfLIS(self, nums):
    n = len(nums)
    if n <= 1:
      return n
    # [0], [1], [k] records best k-length list
    # minimum last number 
    result = [nums[0]]
    for i in range(1, n):
      item = nums[i]
      # change the while loop to binary-search
      # we can get O(nlogn)
      j = len(result) -1 
      while(j>=0):
        # append a new one if possible
        if item > result[-1]:
          result.append(item)
        if j==0:
          result[0] = min(result[0], item)
        elif item>result[j-1] and item<result[j]:
          result[j] = item
        j -= 1
      print i, result
    return len(result)


if __name__ == '__main__':
  a = Solution()
  print a.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
