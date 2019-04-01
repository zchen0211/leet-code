"""
540. Single Element in a Sorted Array (Medium)

Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10

Note: Your solution should run in O(log n) time and O(1) space.
"""

"""
l, r = 0, n-1
while l < r:
  mid = (l + r) // 2
  if mid % 2 == 1: mid -= 1
  if nums[mid] == nums[mid+1]: r = mid
  else: l = mid + 2
return nums[l]
"""


class Solution(object):
  def singleNonDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n == 1: return nums[0]
    st = 0
    end = n
    while st+1 < end:
      mid = (st+end) / 2
      if nums[mid]!=nums[mid-1]: # 0,1,...,mid-1
        if mid % 2 == 0: st = mid
        else: end = mid
      else:
        if mid % 2 == 0: end = mid
        else: st = mid
    # start
    if nums[max(0,st-1):min(n,st+2)].count(nums[st]) == 1:
      return nums[st]
    else:
      return nums[end]
  
if __name__ == '__main__':
  a = Solution()
  print a.singleNonDuplicate([1,1,2,3,3,4,4,8,8])
  print a.singleNonDuplicate([3,3,7,7,10,11,11])
  print a.singleNonDuplicate([3])
  print a.singleNonDuplicate([3,4,4,5,5])
  print a.singleNonDuplicate([4,4,5,5,6])
