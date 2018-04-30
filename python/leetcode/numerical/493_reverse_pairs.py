"""
493. Reverse Pairs (Hard)

Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
Note:
The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.
"""

class Solution(object):
  def reversePairs(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    self.cnt = 0
    self.mergesort(nums, 0, len(nums)-1)
    return self.cnt

  def mergesort(self, nums, i, j):
    if i >= j: return
    if i+1 == j:
      if nums[i] > nums[j]*2: self.cnt += 1
      nums[i], nums[j] = min(nums[i],nums[j]), max(nums[i], nums[j])
      return
    print nums, 'tackling', nums[i:j+1]
    mid = (i+j)/2
    self.mergesort(nums, i, mid)
    self.mergesort(nums, mid+1, j)
    # statistics of reverse pairs
    nums1 = nums[i:mid+1]
    nums2 = nums[mid+1:j+1]
    print nums1, nums2
    i1, i2 = 0, 0
    n1, n2 = len(nums1), len(nums2)
    while i1 < n1 and i2 < n2:
      if nums1[i1] > 2*nums2[i2]:
        self.cnt += n1-i1
        i2 += 1
      else:
        i1 += 1
    nums3 = []
    i1, i2 = 0, 0
    while i1 < n1 or i2 < n2:
      if i1 == n1 or (i2!=n2 and nums2[i2]<nums1[i1]):
        nums3.append(nums2[i2])
        i2 += 1
      else:
        nums3.append(nums1[i1])
        i1 += 1
    print 'nums3', nums3
    nums[i:j+1] = nums3


if __name__ == '__main__':
  a = Solution()
  print a.reversePairs([1, 3, 2, 3, 1])
  print a.reversePairs([2, 4, 3, 5, 1])
