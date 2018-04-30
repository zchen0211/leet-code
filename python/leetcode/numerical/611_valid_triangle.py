"""
611. Valid Triangle Number (Medium)

Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Note:
The length of the given array won't exceed 1000.
The integers in the given array are in the range of [0, 1000].
"""

class Solution(object):
  def triangleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    n = len(nums)
    cnt = 0
    i = 0
    while i<n and nums[i] == 0:
      i += 1
    if i==n: return 0
    
    while i<n:
      k = n - 1
      j = k - 1
      while j>i:
        # count k satisfy nums[i]+nums[j] > nums[k]
        while k>=j and nums[i]+nums[j]<=nums[k]:
          k -= 1
        cnt += k-j
        # print i, j, k, ';', nums[i],nums[j],nums[k],';', cnt
        # print i, j, k, ';', cnt
        j -= 1
      i += 1
    return cnt

if __name__ == '__main__':
  a = Solution()
  print a.triangleNumber([2,2,3,4])
  print a.triangleNumber([1,1,3,4])
