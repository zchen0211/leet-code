'''
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 <= k <= number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''

import collections

class Solution(object):
  def topKFrequent(self, nums, k):
    n = len(nums)
    if n == 0: return []
    if n == 1: return nums
    cnt = collections.Counter(nums)
    cnt = dict(cnt)

    # change to tuple
    cnt = [(a,cnt[a]) for a in cnt.keys()]
    # keep top k
    cnt.sort(key=lambda (k,v): v, reverse=True)
    cnt = cnt[:k]
    cnt = [k for k, v in cnt]
    return cnt

if __name__ == '__main__':
  a = Solution()
  print a.topKFrequent([1,1,2,2,2,3], 2)
