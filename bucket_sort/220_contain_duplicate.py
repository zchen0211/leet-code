'''
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.
'''

class Solution(object):
  def containDuplicate(self, nums, k, t):
    if t<0:
      return False
    bucket = {}
    n = len(nums)
    for i in range(n):
      b_id = nums[i]/(t+1)
      if b_id in bucket:
        return True
      if b_id-1 in bucket:
        if nums[i]-bucket[b_id-1]<=t:
          return True
      if b_id+1 in bucket:
        if bucket[b_id+1]-nums[i]<=t:
          return True
      # add to the bucket and remove to keep only k+1 items
      bucket[b_id] = nums[i]
      if i>=k:
        b_id = nums[i-k]/(t+1)
        del bucket[b_id]
      print i, bucket
    return False


if __name__ == '__main__':
  a = Solution()
  print a.containDuplicate([1,2], 0, 1)
