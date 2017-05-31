"""
592. Fraction Addition and Subtraction (Medium)

Given a string representing an expression of fraction addition and subtraction, you need to return the calculation result in string format. The final result should be irreducible fraction. If your final result is an integer, say 2, you need to change it to the format of fraction that has denominator 1. So in this case, 2 should be converted to 2/1.

Example 1:
Input:"-1/2+1/2"
Output: "0/1"

Example 2:
Input:"-1/2+1/2+1/3"
Output: "1/3"

Example 3:
Input:"1/3-1/2"
Output: "-1/6"

Example 4:
Input:"5/3+1/3"
Output: "2/1"
Note:
The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
Each fraction (input and output) has format +/-numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1,10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
The number of given fractions will be in the range [1,10].
The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.
"""

class Solution(object):
  def defactor(self, result):
    for i in range(2, 11):
      while(result[0] % i == 0 and result[1] %i == 0):
        result = [result[0]/i, result[1]/i]
    return result

  def fractionAddition(self, expression):
    """
    :type expression: str
    :rtype: str
    """
    result = [0, 1] # 0/1 == 0

    i = 0
    n = len(expression)
    while(i < n):
      # +, -
      if i==0 and expression[i] != '-':
        pos_flag = True
      elif i!=0 and expression[i] == '+':
        i += 1
        pos_flag = True
      else:
        i += 1
        pos_flag = False
      # print 'current: ', expression[i:]
      # print 'positive?', pos_flag
      # num
      j = i
      while(j<n and expression[j]!='/'):
        j += 1
      # print 'numerator', expression[i:j]
      numerator = int(expression[i:j])
      i = j+1
      # denominator
      j = i
      while(j<n and expression[j] not in ['+','-']):
        j += 1
      denominator = int(expression[i:j])
      # print 'denominator', expression[i:j]
      # add or sub
      tmp1, tmp2 = result
      if pos_flag:
        result = [tmp1*denominator+tmp2*numerator, tmp2*denominator]
      else:
        result = [tmp1*denominator-tmp2*numerator, tmp2*denominator]
      result = self.defactor(result)
      # update i
      i = j
    # common factor
    if result[0] == 0: result[1] = 1
    else:
      for i in range(11,1, -1):
        if result[0] % i == 0 and result[1] % i == 0:
          result = [result[0]/i, result[1]/i]
    # to string
    str_result = str(result[0])+'/'+str(result[1])
    return str_result

if __name__ == '__main__':
  a = Solution()
  print a.fractionAddition("-1/2+1/2")
  print a.fractionAddition("-1/2+1/2+1/3")
  print a.fractionAddition("1/3-1/2")
  print a.fractionAddition("5/3+1/3")
  print a.fractionAddition("2/5+1/5+7/10+1/5+1/2")

