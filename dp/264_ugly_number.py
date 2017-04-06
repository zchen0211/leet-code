'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number, and n does not exceed 1690.
'''

class Solution(object):
  def nthUglyNumber(self, n):
    if n == 0:
      return 0

    result = [1]
    ind2 = 0
    ind3 = 0
    ind5 = 0

    for i in range(n):
      tmp = min(result[ind2]*2, result[ind3]*3, result[ind5]*5)
      result.append(tmp)
      if tmp == result[ind2]*2:
        ind2 += 1
      if tmp == result[ind3]*3:
        ind3 += 1
      if tmp == result[ind5]*5:
        ind5 += 1
      print tmp
    return result[n-1]


if __name__ == '__main__':
  a = Solution()
  print a.nthUglyNumber(10)
