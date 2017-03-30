'''
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
'''

class Solution(object):
  def helper(self, nums, i, j):
    if i==j:
      return [[nums[i]]]
    mid = (i+j)/2
    if nums[mid]-nums[i] == mid-i:
      res_l = [[nums[i],nums[mid]]]
    else:
      res_l = self.helper(nums, i,mid)

    if nums[mid+1]-nums[j] == mid+1-j:
      res_r = [[nums[mid+1], nums[j]]]
    else:
      res_r = self.helper(nums, mid+1, j)
    # merge if needed
    if res_l[-1][1] == res_r[0][0]-1:
      res_l[-1][1] = res_r[0][1]
      del res_r[0]
    return res_l + res_r

  def summary(self, nums):
    if len(nums) == 0:
      return []
    res_ = self.helper(nums, 0, len(nums)-1)
    result = []
    for item in res_:
      if len(item) == 1 or item[0]==item[1]:
        result.append(str(item[0]))
      else:
        result.append(str(item[0])+'->'+str(item[1]))
    return result

if __name__ == '__main__':
  a = Solution()
  print a.summary([0,1,2,4,5,7])
