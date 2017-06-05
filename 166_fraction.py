'''
166. Fraction to Recurring Decimal (Medium)

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
'''

class Solution(object):
  def fractionToDecimal(self, numerator, denominator):
    if numerator == 0:
      return '0'
    if (numerator>0 and denominator>0) or (numerator<0 and denominator<0):
      neg_flag = False
    else:
      neg_flag = True
    print neg_flag
    numerator = abs(numerator)
    denominator = abs(denominator)

    quo = str(numerator//denominator)
    if numerator % denominator != 0:
      tmp_str = ''
      rem = numerator % denominator
      i = 0 #
      rem_dict = {} # rem to i
      while(True):
        rem = rem*10
        if rem == 0:
          break
        if rem in rem_dict:
          # tackle tmp_str with ()
          tmp_id = rem_dict[rem]
          tmp_str = tmp_str[:tmp_id] + '(' + tmp_str[tmp_id:] + ')'
          break
        else:
          new_q = rem // denominator
          tmp_str += str(new_q)
          rem_dict[rem] = i
          rem = rem % denominator
          i += 1
      quo += '.' + tmp_str
    if neg_flag:
      quo = '-'+quo
    return quo


if __name__ == '__main__':
  a = Solution()
  print a.fractionToDecimal(1, 2)
  print a.fractionToDecimal(2, 1)
  print a.fractionToDecimal(2, 3)
  print a.fractionToDecimal(5, 6)
  print a.fractionToDecimal(5, -6)
  print a.fractionToDecimal(5, 7)
  print a.fractionToDecimal(-50, 8)
