"""
697. Degree of an Array (Easy)

Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""

class Solution(object):
  def findShortestSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    stat = {}
    n = len(nums)
    max_deg = 0
    for i in range(n):
      item = nums[i]
      if item in stat:
        stat[item].append(i)
      else:
        stat[item] = [i]
    for k in stat.keys():
      max_deg = max(max_deg, len(stat[k]))

    ret = n
    for k in stat.keys():
      if len(stat[k]) == max_deg:
        ret = min(stat[k][-1] - stat[k][0] + 1, ret)
    return ret


if __name__ == "__main__":
  a = Solution()
  print a.findShortestSubArray([1, 2, 2, 3, 1])
  print a.findShortestSubArray([1,2,2,3,1,4,2])
