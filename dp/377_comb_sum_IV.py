'''
377. Combination Sum IV (Medium)

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.

Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
'''

class Solution(object):
  def combinationSum4(self, nums, target):
    '''
    input: List[int]
    rtype: int
    '''
    result = [0]
    nums.sort()
    for i in range(1, target+1):
      tmp = 0
      for item in nums:
        if i-item > 0:
          tmp += result[i-item]
        elif i-item == 0:
          tmp += 1
      result.append(tmp)
    return result[-1]


if __name__ == '__main__':
  a = Solution()
  print a.combinationSum4([1,2,3], 4)
