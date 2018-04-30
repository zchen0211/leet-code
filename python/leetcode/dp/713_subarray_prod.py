"""
713. Subarray Product Less Than K (Medium)

Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
"""

from math import log

class Solution(object):
  def numSubarrayProductLessThanK(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    n = len(nums)
    if n == 0: return 0
    if k <= 0: return 0

    accu = [0.]
    for item in nums:
      accu.append(accu[-1] +log(item))

    logk = log(k-0.5)
    print accu, logk

    ret = 0
    i = 0
    j = i + 1
    while i < n:
      while j < n and accu[j] - accu[i] < logk:
        j += 1
      # if j != n+1:
      #   j -= 1
      # nums[i..j]
      if accu[j] - accu[i] < logk:
        ret += 1
        print nums[i:j],
      else:
        print nums[i:j-1],
      ret += max(j-i-1, 0)
      print ret, max(j-i-1, 0)
      i += 1
    # if nums[-1] < k:
    #   ret += 1
    return ret

if __name__ == "__main__":
  a = Solution()
  print a.numSubarrayProductLessThanK([10, 5, 2, 6], 100)
  print a.numSubarrayProductLessThanK([10, 5, 2, 6, 101, 2], 100)
  print a.numSubarrayProductLessThanK([10, 5, 2, 6], 1)
  print a.numSubarrayProductLessThanK([10, 5, 2, 6], 0)
  arr = [10,3,3,7,2,9,7,4,7,2,8,6,5,1,5]
  target = 30
  print a.numSubarrayProductLessThanK(arr, target)
