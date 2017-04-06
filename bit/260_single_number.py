'''
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
'''

class Solution(object):
  def singleNumber(self, nums):
    xor = 0
    # nums
    for item in nums:
      xor = xor ^ item
    print xor
    # find the 1st bit
    bit = 1
    while(bit & xor == 0):
      bit = bit<<1
    res = [0,0]
    for item in nums:
      if item & bit == 0:
        res[0] = res[0] ^ item
      else:
        res[1] = res[1] ^ item
    return res


if __name__ == '__main__':
  a = Solution()
  print a.singleNumber([1,2,1,3,2,5])
