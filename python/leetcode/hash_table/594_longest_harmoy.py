'''
594. Longest Harmonious Subsequence (Easy)

We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Note: The length of the input array will not exceed 20,000.
'''

import collections

class Solution(object):
  def findLHS(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n <= 1: return 0

    num_cnt = dict(collections.Counter(nums))

    result = 0
    for k in num_cnt.keys():
      if k+1 in num_cnt:
        result = max(result, num_cnt[k]+num_cnt[k+1])
    return result

if __name__ == '__main__':
  a = Solution()
  print a.findLHS([1,3,2,2,5,2,3,7])
