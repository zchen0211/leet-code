'''
Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example:
(1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6]. 
(2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
'''

import numpy as np
class Solution(object):
  def wiggleSort(self, nums):
    nums.sort()
    half = len(nums[::2])
    nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]

  def wiggleSort2(self, nums):
    n = len(nums)
    if n>1:
      med = np.median(nums)
    print 'median: ', med
    # ids = []
    small = []
    large = []
    medians = []
    for num in nums:
      if num < med:
        small.append(num)
      elif num > med:
        large.append(num)
    print small
    print large
    '''
    small = 0
    large = n-1
    while(small<large):
      while(small<large and nums[small]<med):
        small += 1
      while(large>small and nums[large]>med):
        large -= 1
      if small<large and nums[small]>nums[large]:
        nums[small], nums[large] = nums[large], nums[small]
        small += 1
        large -= 1
    '''
    # swig
    

if __name__ == '__main__':
  a = Solution()
  print a.wiggleSort([1,5,1,1,6,4])
  print a.wiggleSort([1,3,2,2,3,1])
