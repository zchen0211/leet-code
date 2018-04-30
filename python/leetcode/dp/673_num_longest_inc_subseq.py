"""
673. Number of Longest Increasing Subsequence (Medium)

Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int."""

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0

        seq = [max(nums)+1] * n
        stat = []
        for i in range(n): stat.append({})

        seq[0] = nums[0]
        stat[0][nums[0]] = 1

        curr_len = 1
        for i in range(1, n):
          item = nums[i]
          # look up update stat
          id_ = self.lookup(seq, curr_len, item)
          # print item, seq, id_
          seq[id_] = item

          if id_ == 0: inc = 1
          else:
            inc = 0
            for k in stat[id_-1].keys():
                if k < item:
                    inc += stat[id_-1][k]

          if item in stat[id_]:
            stat[id_][item] += inc
          else:
            stat[id_][item] = inc
          # print 'after', item, seq, id_, stat
          if id_ == curr_len:
            curr_len += 1
        return sum(stat[curr_len-1].values())
    
    def lookup(self, seq, curr_len, item):
        # look up in seq[0:curr_len]
        # search id_ s.t. seq[id_] >=  item
        i = 0
        j = curr_len
        while i < j:
          mid = (i + j) / 2
          if seq[mid] == item: return mid
          elif seq[mid] < item:
            i = mid + 1
          else:
            j = mid
        return i
