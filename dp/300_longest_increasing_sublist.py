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
    """
    :type nums: List[int]
    :rtype: int
    """
    # AC, old version
    n = len(nums)
    if n <= 1:
      return n
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

  def solve2(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # AC, new version, much faster
    n = len(nums)
    if n <= 1: return n
    best_seq = [nums[0]]
    curr_seq = [nums[0]]
    i = 1
    while i<n:
      if nums[i] > best_seq[-1]: best_seq.append(nums[i])

      if nums[i] > curr_seq[-1]: curr_seq.append(nums[i])
      else:
        while len(curr_seq)>0 and curr_seq[-1]>=nums[i]:
          curr_seq.pop()
        curr_seq.append(nums[i])
      if (len(curr_seq)>len(best_seq)) or (len(curr_seq)==len(best_seq) and curr_seq[-1]<best_seq[-1]):
        best_seq = [item for item in curr_seq]
      i += 1
      print best_seq, curr_seq
    return len(best_seq)


if __name__ == '__main__':
  a = Solution()
  print 'old'
  print a.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
  print 'new'
  print a.solve2([10, 9, 2, 5, 3, 7, 101, 18])
