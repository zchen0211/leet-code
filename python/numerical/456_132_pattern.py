'''
456. 132 Pattern (Medium)

Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.
Example 2:
Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:
Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
'''

class Solution(object):
  def find132pattern2(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    n = len(nums)
    if n<=2: return False

    # stack to save num2
    stack = [nums[-1]]
    n3 = None

    # dp
    i = n-2
    while(i>=0):
      if nums[i] > stack[-1]:
        n3 = nums[i]
        while(len(stack)>1 and nums[i]>stack[-2]):
          stack.pop()
      elif nums[i] < stack[-1]:
        if n3 is not None:
          print 'step ', i, nums[i], n3, stack
          return True
        else: stack.append(nums[i])
      print 'step ', i, nums[i], n3, stack
      i -= 1
    return False

  def find132pattern(self, nums):
    n = len(nums)
    if n <= 2: return False
    # find 132 pattern
    n2 = []
    n3 = min(nums) - 1
    print nums
    i = n-1
    while(i>=0):
      if nums[i] < n3:
        return True
      else:
        # pop too small things out
        while(len(n2)>0 and nums[i]>n2[-1]):
          n3 = n2[-1]
          n2.pop()
        n2.append(nums[i])
      print 'step: ', i, 'n2', n2, 'n3', n3, 'current', nums[i]
      i -= 1
    return False


if __name__ == '__main__':
  a = Solution()
  '''print a.find132pattern([-2,1,2,-2,1,2])
  print a.find132pattern([1,2,3,4]) # False
  print a.find132pattern([3,1,4,2]) # True
  print a.find132pattern([-1,3,2,0]) # True
  print a.find132pattern([1,0,1,-4,-3]) # False
  print a.find132pattern([3,5,0,3,4]) # True'''
  print a.find132pattern([10,12,6,8,3,11]) # True
  # print a.find132pattern([-2, 1, 1, -2, 1, 1]) # False
  # print a.find132pattern([2, 4, 3, 1]) # True
