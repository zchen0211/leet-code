'''
152. Maximum Product Subarray (Medium)

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

'''

class Solution(object):
  def maxProduct(self, nums):
    if len(nums) == 1:
      return nums[0]

    zero_flag = False
    big_neg = 0
    big_pos = 0

    best_ever = nums[0]
    n = len(nums)

    for i in range(n):
      if nums[i] > 0:
        big_pos, big_neg = max(big_pos*nums[i], nums[i]), big_neg*nums[i]
        best_ever = max(best_ever, big_pos)
      elif nums[i] < 0:
        big_pos, big_neg = big_neg*nums[i], min(big_pos*nums[i], nums[i])
        best_ever = max(best_ever, big_pos)
      else:
        zero_flag = True
        big_pos = 0
        big_neg = 0
        best_ever = max(0, best_ever)
      print big_neg, big_pos
      
    return best_ever


if __name__ == '__main__':
  a = Solution()
  print a.maxProduct([2,3,-2,-4]) 
