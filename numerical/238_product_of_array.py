'''
238. Product of Array Except Self (Medium)

Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
'''
class Solution(object):
  def productExceptSelf(self, nums):
    n = len(nums)
    left = [1]
    # left[i]: nums[0]*...*nums[i-1]
    for i in range(n-1):
      left.append(left[-1]*nums[i])
    right = [1]
    # right[i]: nums[n-i]*...*nums[n-1]
    for j in range(n-1,0,-1):
      right.append(right[-1]*nums[j])
    result = []
    for i in range(n):
      result.append(left[i]*right[n-i-1])
    return result


if __name__ == '__main__':
  a = Solution()
  print a.productExceptSelf([1,2,3,4])
