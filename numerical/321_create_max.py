'''
321. Create Maximum Number (Hard)

Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits. You should try to optimize your time and space complexity.

Example 1:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
return [9, 8, 6, 5, 3]

Example 2:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
return [6, 7, 6, 0, 4]

Example 3:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
return [9, 8, 9]
'''

class Solution(object):
  def maxNumber(self, nums1, nums2, k):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :type k: int
    :rtype: List[int]
    """
    n1 = len(nums1)
    n2 = len(nums2)
    result = None
    for i in range(0, k+1):
      # nums1: i, nums2: k-i
      if n1 < i or n2 < k-i:
        continue
      elif i == 0:
        tmp_ = self.helper(nums2, k)
      elif i == k:
        tmp_ = self.helper(nums1, k)
      else:
        tmp1_ = self.helper(nums1, i)
        tmp2_ = self.helper(nums2, k-i)
        print '1', tmp1_
        print '2', tmp2_
        tmp_ = self.merge(tmp1_, tmp2_)
      print tmp_
      if result is None or str(tmp_) > str(result):
        result = tmp_
    return result

  def merge(self, tmp1_, tmp2_):
    tmp_ = []
    i1, i2 = 0, 0
    n1_, n2_ = len(tmp1_), len(tmp2_)
    while i1 != n1_ or i2 != n2_:
      if self.greater(tmp1_, i1, tmp2_, i2):
        tmp_.append(tmp1_[i1])
        i1 += 1
      else: 
        tmp_.append(tmp2_[i2])
        i2 += 1
    return tmp_

  def greater(self, tmp1_, i1, tmp2_, i2):
    while i1!=len(tmp1_) and i2!=len(tmp2_) and tmp1_[i1]==tmp2_[i2]:
      i1, i2 = i1+1, i2+1
    return i2 == len(tmp2_) or (i1 < len(tmp1_) and tmp1_[i1] > tmp2_[i2]);


  def helper(self, nums1, k):
    result = [0] * (k+1)
    n = len(nums1)
    if n == k:
      result = [item for item in nums1]
      return result
    for i in range(n):
      tmp = nums1[i]
      j = min(i + 1, k)
      while j > 0:
        result[j] = max(result[j], result[j-1]*10+nums1[i])
        j -= 1

    result = result[-1]
    l_ = []
    while result > 0:
      l_.append(int(result%10))
      result /= 10
    l_ = l_[::-1]
    return l_


if __name__ == "__main__":
  a = Solution()
  # print a.maxNumber([1,2], [], 2)
  # print a.maxNumber([1,2], [1,3], 4)
  # print a.maxNumber([0,0,7], [0,1], 5)
  # print a.maxNumber([2,1,7,8,0,1,7,3,5,8,9,0,0,7,0,2,2,7,3,5,5],[2,6,2,0,1,0,5,4,5,5,3,3,3,4],35)
  print a.maxNumber([8,0,4,4,1,7,3,6,5,9,3,6,6,0,2,5,1,7,7,7,8,7,1,4,4,5,4,8,7,6,2,2,9,4,7,5,6,2,2,8,4,6,0,4,7,8,9,1,7,0],[6,9,8,1,1,5,7,3,1,3,3,4,9,2,8,0,6,9,3,3,7,8,3,4,2,4,7,4,5,7,7,2,5,6,3,6,7,0,3,5,3,2,8,1,6,6,1,0,8,4],50)
  # print a.maxNumber([2,5,6,4,4,0], [7,3,8,0,6,5,7,6,2], 15)
  # print a.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5)
  # print a.maxNumber([6, 7], [6,0,4], 5)
  # print a.maxNumber([3, 9], [8,9], 3)
  # print a.helper([9,1,2,5,8,3], 3) 
  # print a.helper([3,4,6,5], 2)
  print a.maxNumber([1,5,8,1,4,0,8,5,0,7,0,5,7,6,0,5,5,2,4,3,6,4,6,6,3,8,1,1,3,1,3,5,4,3,9,5,0,3,8,1,4,9,8,8,3,4,6,2,5,4,1,1,4,6,5,2,3,6,3,5,4,3,0,7,2,5,1,5,3,3,8,2,2,7,6,7,5,9,1,2],[7,8,5,8,0,1,1,6,1,7,6,9,6,6,0,8,5,8,6,3,4,0,4,6,7,8,7,7,7,5,7,2,5,2,1,9,5,9,3,7,3,9,9,3,1,4,3,3,9,7,1,4,4,1,4,0,2,3,1,3,2,0,2,4,0,9,2,0,1,3,9,1,2,2,6,6,9,3,6,0],80) 
