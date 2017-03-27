'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''


class Solution(object):
  def addStrings(self, num1, num2):
    num1 = num1[::-1]
    num2 = num2[::-1]
    result = ''
    i = 0
    carry_flag = False
    while(i<len(num1) or i<len(num2)):
      if i<len(num1) and i<len(num2):
        tmp = int(num1[i]) + int(num2[i])
      elif i<len(num1):
        tmp = int(num1[i])
      elif i<len(num2):
        tmp = int(num2[i])
      if carry_flag:
        tmp += 1
      if tmp >= 10:
        carry_flag = True
        tmp -= 10
      else:
        carry_flag = False
      i += 1
      result += str(tmp)
    if carry_flag:
      result += '1'
    result = result[::-1]
    return result


if __name__ == '__main__':
  a = Solution()
  print a.addStrings('1', '12345')
