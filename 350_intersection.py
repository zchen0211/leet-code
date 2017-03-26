import collections


class Solution(object):
  def intersect(self, nums1, nums2):
    cmap1 = dict(collections.Counter(nums1))
    cmap2 = dict(collections.Counter(nums2))
    result = []
    for k, v in cmap1.items():
      if cmap2.has_key(k):
        result += [k] * min(v, cmap2[k])
    return result


if __name__ == '__main__':
  a = Solution()
  print a.intersect([1,1,2,2],[2,2])
