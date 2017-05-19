'''
273. Integer to English Words

Total Accepted: 35305
Total Submissions: 162625
Difficulty: Hard
Contributor: LeetCode
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
  
  def helper(self, num):
    result = ''
    # 0 - 999
    map1 = {1:'One', 2:'Two', 3: 'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine'}
    map2 = {10: 'Ten', 11:'Eleven', 12:'Twelve', 13: 'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen'}
    map3 = {20: 'Twenty', 30:'Thirty', 40: 'Forty', 50:'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90:'Ninety'}

    if num>=100:
      tmp = num / 100
      result += map1[tmp] + ' Hundred'
      num = num % 100
    if num>=10 and num<=19:
      if result != '': result += ' '
      result += map2[num]
      num = 0
    if num>=20:
      tmp = num / 10
      if result != '': result += ' '
      result += map3[tmp*10]
      num = num % 10
    if num in map1:
      if result != '': result += ' '
      result += map1[num]
    return result


if __name__ == '__main__':
  a = Solution()
  print a.numberToWords(123)
  print a.numberToWords(12345)
  print a.numberToWords(1234567)
  print a.numberToWords(1234567891)
