class Solution(object):
  def minMoves(self, nums):
    min_num = min(nums)
    result = sum(nums) - len(nums) * min_num
    return result


if __name__ == '__main__':
  a = Solution()
  print a.minMoves([1,2,4])
