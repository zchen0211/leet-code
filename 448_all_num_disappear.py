class Solution(object):
  def findDisappear(self, nums):
    # put everything into a set
    num_set = set(nums)
    all_set = set(range(1, len(nums)+1))
    dis_set = all_set - num_set
    return list(dis_set)


if __name__ == '__main__':
  a = Solution()
  print a.findDisappear([4,3,2,7,8,2,3,1])
  print a.findDisappear([1,1])
  
