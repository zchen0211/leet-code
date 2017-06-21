"""
503. Next Greater Element II (Medium)

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
"""
# notice while None in result will spend a lot of time
class Solution(object):
  def nextGreaterElements(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n = len(nums)
    result = [None]*n
    stack = []
    i = 0
    nums_max = max(nums)
   
    cnt = 0 
    while cnt < 2*n:
      if nums[i] == nums_max:
        result[i] = -1
        cnt += 1
      while len(stack)>0 and nums[i] > nums[stack[-1]]:
        tmp = stack.pop()
        result[tmp] = nums[i]
        cnt += 1
      stack.append(i)
      i = (i+1) % n
      cnt += 1
    return result


if __name__ == '__main__':
  a = Solution()
  print a.nextGreaterElements([1,2,1])
  print a.nextGreaterElements([1,2,3,2,1])
