'''
189. Rotate Array (Easy)

Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
'''

class Solution(object):
  def rotate(self, nums, k):
    k = k % len(nums) # a must!
    nums[:] = nums[-k:] + nums[:-k]


if __name__ == '__main__':
  a = Solution()
  print a.rotate(range(1,3), 1)
