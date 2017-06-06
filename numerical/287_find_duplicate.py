'''
287. Find the Duplicate Number (Medium)

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
'''

class Solution(object):
  def findDuplicate(self, nums):
    slow = nums[0]
    fast = nums[slow]
    while(fast != slow):
      slow = nums[slow]
      fast = nums[fast]
      fast = nums[fast]
    print fast
    fast = 0
    while(slow != fast):
      fast = nums[fast]
      slow = nums[slow]
    return slow


if __name__ == '__main__':
  a = Solution()
  print a.findDuplicate([1,4,2,3,5,1])
