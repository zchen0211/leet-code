import math


class Solution(object):
  def findNthDigit(self, n):
    # 1-9: 1-9; cumul (9)
    # 10-99: cumul + 90 x 2; cumul 189
    # 100-999: cumul + 900 x 3; cumul
    i = 1
    cumul = 0

    while(i<11): # i-digit case
      cumul_after = cumul + i*9*(10**(i-1))
      if n>=cumul and n<=cumul_after:
        # figure out which number
        start = 10**(i-1)
        num = start + (n-cumul+i-1) // i - 1
        print start, num
        # figure out which digit
        k = (n-cumul-1) % i
        return int(str(num)[k])
      else:
        cumul = cumul_after
        i += 1
    return result


if __name__ == '__main__':
  a = Solution()
  print a.findNthDigit(5)
  print a.findNthDigit(11)
