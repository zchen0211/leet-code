'''
179. Largest Number (Medium)

Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
'''

class Solution(object):
  def largestNumber(self, nums):
    nums = [str(item) for item in nums]
    # sort in reverse order
    nums.sort(cmp=lambda x, y: cmp(y+x, x+y))
    result = ''.join(nums)
    result = result.lstrip('0')
    if len(result) == 0:
      return '0'
    else
      return result
