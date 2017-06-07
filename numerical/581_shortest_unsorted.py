'''
581. Shortest Unsorted Continuous Subarray (Easy)

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
Subscribe to see which companies asked this question.

'''

class Solution(object):
  def findUnsorted(self, nums):
    '''
    : type nums: List[int]
    : rtype: int
    '''
    # AC: Best solution
    # pay attention to the searching order for min_ and max_!

    # to find end: if a num[j] < max[0..j-1], end update as j
    # to find begin: if a num[i]
    n = len(nums)
    if n <= 1: return 0
    begin, end = -1, -1
    max_, min_ = nums[0], nums[n-1]
    for i in range(1,n):
      max_ = max(max_, nums[i])
      min_ = min(min_, nums[n-i-1])
      if nums[i] < max_:
        end = i
      if nums[n-i-1] > min_:
        begin = n-i-1
    if begin == -1: return 0
    else: return end-begin+1

if __name__ == '__main__':
  a = Solution()
  print a.findUnsorted2([2,6,4,8,10,9,15])
  # print a.findUnsorted2([2,1])
  # print a.findUnsorted2([1,2,3,3,3])
