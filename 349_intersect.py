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
