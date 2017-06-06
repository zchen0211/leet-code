'''
349 Intersection of Two Arrays (Easy)

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
Subscribe to see which companies asked this question.
'''


class Solution(object):
  def intersect(self, nums1, nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)
    result = []
    for k in nums1:
      if k in nums2:
        result.append(k)
    return result


if __name__ == '__main__':
  a = Solution()
  print a.intersect([1,1],[2,2,1,1])
