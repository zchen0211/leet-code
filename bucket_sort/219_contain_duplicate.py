'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
'''

class Solution(object):
  def contain(self, nums, k):
    if len(nums) <= k+1:
      if len(set(nums)) == len(nums):
        return False
      else:
        return True
    if k==0:
      return False
    st = 0
    end = k
    tmp_set = set([])
    while(end != len(nums)):
      if st == 0:
        tmp_set = set(nums[st:end+1])
      else:
        tmp_set.remove(nums[st-1])
        tmp_set.add(nums[end])
      if len(tmp_set) != k+1:
        return True
      st += 1
      end += 1
    return False
