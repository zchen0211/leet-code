'''
462. Minimum Moves to Equal Array Elements II (Medium)

Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
'''
class Solution(object):
  def minMoves2(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # find median
    nums.sort()
    n = len(nums)
    if n % 2 == 1:
      k = nums[n/2]
      return sum([abs(item-k) for item in nums])
    else:
      k1 = nums[n/2-1]
      k2 = nums[n/2]
      res1 = sum([abs(item-k1) for item in nums])
      res2 = sum([abs(item-k2) for item in nums])
      return min(res1, res2)


if __name__ == '__main__':
  a = Solution()
  print a.minMoves2([1,2])
