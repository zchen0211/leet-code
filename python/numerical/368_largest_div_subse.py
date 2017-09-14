'''
368. Largest Divisible Subset (Medium)

Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

nums: [1,2,3]

Result: [1,2] (of course, [1,3] will also be ok)
Example 2:

nums: [1,2,4,8]

Result: [1,2,4,8]
'''

class Solution(object):
  def largeDivSubset(self, nums):
    nums.sort()
    n = len(nums)
    if n<=1: return nums
    div_ = {nums[0]:[nums[0]]}

    for i in range(1, n):
      j = i - 1
      tmp_cnt = 0
      tmp_id = -1
      while j >= 0:
        if nums[i] % nums[j] == 0:
          if tmp_cnt < len(div_[nums[j]]):
            tmp_id = j
            tmp_cnt = len(div_[nums[j]])
        j -= 1
      if tmp_id == -1:
        div_[nums[i]] = [nums[i]]
      else:
        div_[nums[i]] = [item for item in div_[nums[tmp_id]]]
        div_[nums[i]].append(nums[i])
      print div_
    # find max
    div_max = 1
    for k in div_.keys():
      div_max = max(div_max, len(div_[k]))
    
    for k in div_.keys():
      print k, len(div_[k])
      if len(div_[k]) == div_max:
        return div_[k]


if __name__ == '__main__':
  a = Solution()
  print a.largeDivSubset([1,2,4,8])
  print a.largeDivSubset([1,2,3])
  print a.largeDivSubset([2,3,4,8])
