'''
421. Maximum XOR of Two Numbers in an Array (Medium)

Given a non-empty array of numbers, a0, a1, a2, ... , an-1, where 0 <= ai < 2^31.

Find the maximum result of ai XOR aj, where 0 <= i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
'''

# take-aways:
# 1. iteration by bit, starting from most significant
# 2. mask: 111..1100..00, all 1 until i-th digit
# 3. tmp: current max_ with new '1' added ath i-th digit to see if achievable
# 4. if tmp achievable, update max_, check tmp^prefix in tmp_set (***)

class Solution(object):
  def findMaximumXOR(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_, mask = 0, 0
    for i in range(31,-1,-1):
      mask = mask | (1<<i)
      tmp_set = set()

      for num in nums:
        tmp_set.add(num & mask)

      tmp = max_ | (1<<i)
      for prefix in tmp_set:
        if tmp^prefix in tmp_set:
          max_ = tmp
          break
      print 'digit', i, 'mask', bin(mask), 'tmp', bin(tmp), 'tmp_set', tmp_set, 'max', bin(max_)
    return max_

  def solution2(self, nums):
    # 
    max_ = 0
    mask = 0
    for n in range(31, -1, -1):
      mask = mask | 1<<n # mask: 11..11 00..00 (n 0s at the end)
      tmp_set = set()
      for num in nums:
        tmp_set.add(num & mask)
      # possible to add a 1 in max_
      tmp_ = max_ | (1<<n)
      for item in tmp_set:
        if item ^ tmp_ in tmp_set:
          max_ = tmp_
          break
    return max_

if __name__ == '__main__':
  a = Solution()
  print a.findMaximumXOR([3,10,5,25,2,8])
  print a.solution2([3,10,5,25,2,8])
