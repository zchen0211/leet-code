class Solution(object):
  def Helper_map(self, x):
    # convert 10-15 to a-f
    if x == 10:
      return 'a'
    elif x == 11:
      return 'b'
    elif x == 12:
      return 'c'
    elif x == 13:
      return 'd'
    elif x == 14:
      return 'e'
    elif x == 15:
      return 'f'
    else:
      return str(x)
  def toHex(self, num):
    result = ''
    if num == 0:
      return '0'
    elif num > 0:
      while(num>0):
        rem = num % 16
        result += self.Helper_map(rem)
        num = num // 16
      result = result[::-1]
    else: # negative case
      num += 1
      num = -num
      result_ = []
      while(num>0):
        rem = num % 16
        result_.append(rem)
        num = num // 16
      result_ = result_[::-1]
      result_ = [0]*(8-len(result_)) + result_
      # revert every bit
      result = ''
      for i in range(8):
        result += self.Helper_map(15-result_[i])
    return result


if __name__ == '__main__':
  a = Solution()
  print a.toHex(26)
  print a.toHex(-2)
