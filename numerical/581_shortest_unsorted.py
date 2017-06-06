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
    if len(nums) <= 1: return 0
    
    i = 0
    st = -1
    while(i<len(nums)):
      if i==0 or nums[i]>=nums[i-1]:
        i += 1
      else:
        if st == -1: st = i-1
        # move st s.t. nums[st]>nums[i], nums[st-1]<nums[i]
        while(st>0 and nums[st-1]>nums[i]):
          st -= 1
        i += 1
      if st == 0: break
    if st == -1: return 0
    print 'start: ', st
    
    end = -1
    j = len(nums) - 1 
    while(j>=0):
      if j==len(nums)-1 or nums[j]<=nums[j+1]:
        j -= 1
      else:
        if end==-1: end = j+1
        while(end<len(nums)-1 and nums[end+1]<nums[j]):
          end += 1
        j -= 1
        print j, end
      if end == len(nums)-1: break
    print 'end: ', end
    return end-st+1

  def findUnsorted2(self, nums):
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
