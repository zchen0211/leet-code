'''
334. Increasing Triplet Subsequence

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k 
such that arr[i] < arr[j] < arr[k] given 0 <= i < j < k <= n-1 else return false.
Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.
'''

class Solution(object):
  def incTriplet(self, nums):
    n = len(nums)
    if n <= 2: return False
    min1 = nums[0]
    min2 = None
    for i in range(1, n):
      min1 = min(min1, nums[i])

      if nums[i] > min1:
        if min2 is None:
          min2 = nums[i]
        else:
          min2 = min(min2, nums[i])
        if nums[i] > min2:
          return True
    return False


if __name__ == '__main__':
  a = Solution()
  print a.incTriplet([1,2,3,4,5])
  print a.incTriplet([5,4,3,2,1])
