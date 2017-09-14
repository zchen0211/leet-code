'''
217. Contains Duplicate (Easy)

Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
'''

class Solution(object):
  def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    a = set(nums)
    if len(a) == len(nums):
        return False
    else:
        return True
