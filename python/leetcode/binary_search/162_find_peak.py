'''
162. Find Peak Element (Medium)

A peak element is an element that is greater than its neighbors.

Given an input array where num[i] != num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -\infty.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
'''

"""
Notice edge condition: num[-1], num[n], neg infinity

divide and conquer.

MIT course with explan
https://www.youtube.com/watch?v=HtSuA80QTyo&feature=youtu.be
"""

class Solution(object):
  def findPeakElement(self, nums):
    if len(nums) == 1:
      return 0

    st = 0
    end = len(nums)-1
    while(st!=end):
      if st == end-1:
        if nums[st]>nums[end]:
          return st
        else:
          return end
      mid = (st+end)/2
      # if nums[st]>nums[mid] and nums[mid]>nums[end]: # sorted
      #  return st
      #elif nums[st]<nums[mid] and nums[mid]<nums[end]:
      #  return end
      if nums[mid-1]<nums[mid]:
        st = mid
      else:
        end = mid
    return st


if __name__ == '__main__':
  a = Solution()
  print a.findPeakElement([1,2,3,4,5,4])
