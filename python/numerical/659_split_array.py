"""
659. Split Array into Consecutive Subsequences (Medium)

You are given an integer array sorted in ascending order (may contain duplicates), you need to split them into several subsequences, where each subsequences consist of at least 3 consecutive integers. Return whether you can make such a split.

Example 1:
Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5
Example 2:
Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5
Example 3:
Input: [1,2,3,4,4,5]
Output: False
Note:
The length of the input is in range of [1, 10000]
"""

class Solution(object):
  def isPossible(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    n = len(nums)
    if n == 0: return False
    result = [[nums[0]]]
    for i in range(1, n):
      k = nums[i]
      k_list = len(result)
      j = k_list - 1
      flag = False
      while j >= 0:
        if result[j][-1] == k-1:
          result[j].append(k)
          flag = True
          break
        elif result[j][-1] != k:
          break
        j -= 1
      if not flag:
        result.append([k])
    print result
    k_list = len(result)
    for i in range(k_list):
      if len(result[i]) < 3: return False
    return True


if __name__ == "__main__":
  a = Solution()
  print a.isPossible([1,2,3,3,4,5])
  print a.isPossible([1,2,3,3,4,4,5,5])
  print a.isPossible([1,2,3,4,4,5])
