'''
330. Patching Array (Hard)

Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number in range [1, n] inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.

Example 1:
nums = [1, 3], n = 6
Return 1.

Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.

Example 2:
nums = [1, 5, 10], n = 20
Return 2.
The two patches can be [2, 4].

Example 3:
nums = [1, 2, 2], n = 5
Return 0.
'''
from collections import Counter

class Solution(object):
  def minPatches(self, nums, n):
    """
    :type nums: List[int]
    :type n: int
    :rtype: int
    """
    # too brute force! will TLE and oom
    if n == 0: return 0
    # nums.sort()
    self.set_ = set([0])
    # step 1: all numbers reachable
    self.reach(nums)
    print self.set_

    # step 2: fill too large hole in the back
    added = []
    max_ = max(self.set_)
    while n > max_*2:
      added.append( (n+1)/2)
      n = n/2
    print added, n

    # step 2: filling the holes
    for i in range(1, n+1):
      if i not in self.set_:
        # update
        new_set = set()
        for item in self.set_:
          if item+i not in self.set_:
            new_set.add(item+i)
        for item in new_set:
          self.set_.add(item)
        added.append(i)
    print added
    return len(added)

  def reach(self, nums):
    # a counter first?
    nums_cnt = dict(Counter(nums))

    for item in nums_cnt.keys():
      n = nums_cnt[item]
      new_set = set()
      for old in self.set_:
        for j in range(1, n+1):
          if item+old*j not in self.set_:
            new_set.add(item+old*j)
      for new in new_set:
        self.set_.add(new)

  def solve2(self, nums, n):
    if n == 0: return 0
    nums.sort()
    miss = 1
    i = 0
    result = 0
    while miss <= n:
      # it is not a miss, add all possible
      if i < len(nums) and nums[i] <= miss:
        miss += nums[i]
        i += 1
      else: # add miss into the system
        result += 1
        miss *= 2
    return result

if __name__ == "__main__":
  a = Solution()
  # print a.minPatches([1,3], 6) 
  print a.solve2([1,3], 6) 
  # print a.minPatches([1,5,10], 20) 
  print a.solve2([1,5,10], 20) 
  # print a.minPatches([1,2,2], 5) 
  print a.solve2([1,2,2], 5) 
  # print a.minPatches([1,2,31,33], 1000)
  print a.solve2([1,2,31,33], 1000) 
  # print a.minPatches([1,2,31,33], 2147483647) 
  print a.solve2([1,2,31,33], 2147483647) 
