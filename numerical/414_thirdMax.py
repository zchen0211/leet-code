'''
414. Third Maximum Number (Easy)

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''

class Solution(object):
  def thirdMax(self, nums):
    if not nums:
      return
    if len(nums) <= 2:
      return max(nums)
    max_3 = set([])
    for num in nums:
      if len(max_3) < 3:
        max_3.add(num)
      elif num > min(max_3) and num not in max_3:
        max_3.remove(min(max_3))
        max_3.add(num)
      print num, max_3
    if len(max_3) < 3:
      return max(max_3)
    else:
      return min(max_3)
    return min(max_3)


if __name__ == '__main__':
  a = Solution()
  # print a.thirdMax([100, 1,3,5,7,9,11])
  # print a.thirdMax([2,2,3,1])
  print a.thirdMax([1, 2,2,5,3,5])
