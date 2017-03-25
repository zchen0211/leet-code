class Solution(object):
  def thirdMax(self, nums):
    if not nums:
      return
    if len(nums) <= 2:
      return max(nums)
    max_3 = set([])
    for num in nums:
      if len(max_3) < 3:
        max_3.add(num)
      elif num > min(max_3) and num not in max_3:
        max_3.remove(min(max_3))
        max_3.add(num)
      print num, max_3
    if len(max_3) < 3:
      return max(max_3)
    else:
      return min(max_3)
    return min(max_3)


if __name__ == '__main__':
  a = Solution()
  # print a.thirdMax([100, 1,3,5,7,9,11])
  # print a.thirdMax([2,2,3,1])
  print a.thirdMax([1, 2,2,5,3,5])
