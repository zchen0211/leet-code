class Solution(object):
  def findComplement(self, num):
    """
    :type num: int
    :rtype: int
    """
    # minimum 111..1 >= num
    all_one = 1
    while(all_one<num):
      all_one = all_one * 2 + 1
    return all_one - num


if __name__ == '__main__':
  a = Solution()
  print a.findComplement(5)
  print a.findComplement(1)
