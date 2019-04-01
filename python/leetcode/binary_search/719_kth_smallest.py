"""
719. Find K-th Smallest Pair Distance (Hard)

Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B.

Example 1:
Input:
nums = [1,3,1]
k = 1
Output: 0 
Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Note:
2 <= len(nums) <= 10000.
0 <= nums[i] < 1000000.
1 <= k <= len(nums) * (len(nums) - 1) / 2.
"""

"""
Trial-and-Error:
1. sort the array O(n logn)
2. solution must be between (0, max(nums)-min(nums))
3. binary search in [left, right]:
  find x s.t. f(x) >= k
"""


class Solution(object):
  def smallestDistancePair(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    nums.sort()
        n = len(nums)
        l, r = 0, nums[-1] - nums[0]
        
        while l < r:
            m = (l + r) // 2
            
            # count how many pairs <= m
            cnt, j = 0, 0
            for i in range(n):
                while j < n and nums[j] <= nums[i] + m:
                    j += 1
                cnt += j - i - 1


if __name__ == "__main__":
  a = Solution()
  print a.smallestDistancePair([1,300,1], 2)
  # print a.smallestDistancePair([62, 100, 4], 2)
