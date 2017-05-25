'''
376. Wiggle Subsequence (Medium)

A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

Examples:
Input: [1,7,4,9,2,5]
Output: 6
The entire sequence is a wiggle sequence.

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].

Input: [1,2,3,4,5,6,7,8,9]
Output: 2

Follow up:
Can you do it in O(n) time?
'''

class Solution(object):
  def wiggleMaxLength(self, nums):
    n = len(nums)
    if n <= 1: return n
    
    # wiggle 1: up first
    # wiggle 2: down first
    wiggle1_end = nums[0]
    wiggle2_end = nums[0]
    wiggle1_act = 'up'
    wiggle2_act = 'down'
    wiggle1_len = 1
    wiggle2_len = 1

    for i in range(1, n):
      # tackle wiggle 1 case
      if nums[i] > wiggle1_end:
        if wiggle1_act == 'up':
          wiggle1_end = nums[i]
          wiggle1_act = 'down'
          wiggle1_len += 1
        else: # down
          wiggle1_end = nums[i]
      elif nums[i] < wiggle1_end:
        if wiggle1_act == 'down':
          wiggle1_end = nums[i]
          wiggle1_act = 'up'
          wiggle1_len += 1
        else: # up
          wiggle1_end = nums[i]
      # tackle wiggle 2 case
      if nums[i] > wiggle2_end:
        if wiggle2_act == 'up':
          wiggle2_end = nums[i]
          wiggle2_act = 'down'
          wiggle2_len += 1
        else: # down
          wiggle2_end = nums[i]
      elif nums[i] < wiggle2_end:
        if wiggle2_act == 'down':
          wiggle2_end = nums[i]
          wiggle2_act = 'up'
          wiggle2_len += 1
        else: # up
          wiggle2_end = nums[i]
    return max(wiggle1_len, wiggle2_len)


if __name__ == '__main__':
  a = Solution()
  print a.wiggleMaxLength([1,7,4,9,2,5])
  print a.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])
  print a.wiggleMaxLength([1,2,3,4,5,6,7,8,9])
