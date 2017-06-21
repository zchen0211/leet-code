"""
457. Circular Array Loop (Medium)

You are given an array of positive and negative integers. If a number n at an index is positive, then move forward n steps. Conversely, if it's negative (-n), move backward n steps. Assume the first element of the array is forward next to the last element, and the last element is backward next to the first element. Determine if there is a loop in this array. A loop starts and ends at a particular index with more than 1 element along the loop. The loop must be "forward" or "backward'.

Example 1: Given the array [2, -1, 1, 2, 2], there is a loop, from index 0 -> 2 -> 3 -> 0.

Example 2: Given the array [-1, 2], there is no loop.

Note: The given array is guaranteed to contain no element "0".

Can you do it in O(n) time complexity and O(1) space complexity?
"""

class Solution(object):
  def circularArrayLoop(self, nums):
    n = len(nums)
    for i in range(n):
      if nums[i] == 0:
        continue
      else:
        if self.helper(nums, i):
          return True
    return False

  def helper(self, nums, start):
    """
    :type nums: List[int]
    :rtype: bool
    """
    n = len(nums)
    if n <= 1: return False
    print 'searching'
    # step 1: meet somewhere
    slow = (start + nums[start]) % n
    fast = (slow + nums[slow]) % n
    print slow, fast
    while slow != fast:
      slow = (slow + nums[slow]) % n
      fast = (fast + nums[fast]) % n
      fast = (fast + nums[fast]) % n
      print slow, fast
    # print slow, fast
    # step 2: beginning of the loop
    fast = start
    while slow != fast:
      slow = (slow + nums[slow]) % n
      fast = (fast + nums[fast]) % n
    print 'meeting: ', slow, fast

    # check 2 things:
    # 1. more than one element in the loop
    ret = True
    if slow == (slow+nums[slow])%n:
      # set eveything as zero along the line
      ret = False
    # print 'pass 1 element check'
    # 2. pure forward or backward
    forward_ = nums[slow]>0
    slow = (slow + nums[slow]) % n
    while slow != fast:
      tmp = nums[slow]
      if (forward_ and tmp<0) or (not forward_ and tmp>0):
        ret = False
        break
      slow = (slow + nums[slow]) % n
    # print 'pass pure forward/backward check'
    if not ret:
      # set everything along as zero
      slow = start
      while nums[slow] != 0:
        slow_next = (slow + nums[slow]) % n
        nums[slow] = 0
        slow = slow_next
    print nums
    return ret

if __name__ == '__main__':
  a = Solution()
  # print a.circularArrayLoop([2,-1,1,2,2])
  # print a.circularArrayLoop([-1,2])
  print a.circularArrayLoop([-2, 1, -1, -2, -2])
  # print a.circularArrayLoop([3,1,2])
