'''
481. Magical String (Easy)

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
'''

# Notice: for i in range(n):
# even if i has been changed in the loop
# will be modified back in for loop
class Solution(object):
  def findMaxConsecutiveOnes(self, nums):
    if len(nums) == 0:
      return 0
    tmp_max = 0
    end_id = 0
    i = 0
    while(i<len(nums)):
      if nums[i] == 1:
        end_id = i
        # end_id goes to the last one
        while(end_id<len(nums)-1 and nums[end_id+1]==1):
          end_id += 1
        tmp_max = max(tmp_max, end_id-i+1)
        i = end_id + 1
        print i
      else:
        i += 1
    return tmp_max


if __name__ == '__main__':
  a = Solution()
  print a.findMaxConsecutiveOnes([1,1,0,1,1,1])
