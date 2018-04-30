'''
273. Integer to English Words (Hard)

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
'''

class Solution(object):
  def numberToWords(self, num):
    if num == 0: return 'zero'

    result = ''
    # billion
    if num >= 1000000000:
      tmp = num / 1000000000
      result += self.helper(tmp)
      result += ' Billion'
      num = num % 1000000000

    # million
    if num >= 1000000:
      tmp = num / 1000000
      if result != '': result += ' '
      result += self.helper(tmp)
      result += ' Million'
      num = num % 1000000

    # thousand
    if num >= 1000:
      tmp = num / 1000
      if result != '': result += ' '
      result += self.helper(tmp)
      result += ' Thousand'
      num = num % 1000
    # hundred
    if num > 0:
      if result != '': result += ' '
      result += self.helper(num)
    return result

  def solution2(self, num):
    if num == 0: return 'Zero'
    result = []
    base = 10**9
    if num > base:
      result.append(self.helper(num/base) + ' Billion')
      num = num % base
    base = 10**6
    if num > base:
      result.append(self.helper(num/base) + ' Million')
      num = num % base
    base = 10**3
    if num > base:
      result.append(self.helper(num/base) + ' Thousand')
      num = num % base
    if num > 0:
      result.append(self.helper(num))
    # print result
    result = ' '.join(result)
    return result
  
  def helper(self, num):
    if num == 0: return 'Zero'
    result = []
    # 0 - 999
    map1 = {1:'One', 2:'Two', 3: 'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10: 'Ten', 11:'Eleven', 12:'Twelve', 13: 'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen'}
    map3 = {20: 'Twenty', 30:'Thirty', 40: 'Forty', 50:'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90:'Ninety'}

    if num >= 100:
      result.append(map1[num/100] + ' Hundred')
      num = num % 100
    if num >= 20:
      result.append(map3[(num/10)*10])
      num = num % 10
    if num<=19 and num>0:
      result.append(map1[num])
    return ' '.join(result)


if __name__ == '__main__':
  a = Solution()
  print a.numberToWords(123)
  print a.solution2(123)
  print a.numberToWords(12345)
  print a.solution2(12345)
  print a.numberToWords(1234567)
  print a.solution2(1234567)
  print a.numberToWords(1234567891)
  print a.solution2(1234567891)
  print a.solution2(0)
  print a.solution2(1000)
