class Solution(object):
  def convertToBase7(self, num):
    """
    :type num: int
    :rtype: str
    """
    if num > 0:
      result = ''
      while(num>0):
        rem = num % 7
        result += str(rem)
        num = num // 7
      result = result[::-1]
      return result
    elif num == 0:
      return '0'
    else: # negative
      result = ''
      while(num<0):
        rem = num%7
        if rem == 0:
          result += str(rem)
          num = num // 7
        else:
          rem = 7 - rem
          result += str(rem)
          num = num // 7 + 1
      result = result[::-1]
      result = '-'+result
      return result


if __name__ == '__main__':
  a = Solution()
  print a.convertToBase7(100)
  print a.convertToBase7(0)
  print a.convertToBase7(-100)
