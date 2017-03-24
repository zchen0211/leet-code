class Solution(object):
  def hammingDis(self, x, y):
    if x == 0 and y == 0:
      return 0
    cnt = 0
    while x > 0 or y > 0:
      x_rem = x % 2
      y_rem = y % 2
      x = x // 2
      y = y // 2
      if x_rem != y_rem:
        cnt += 1
    return cnt


if __name__ == '__main__':
  a = Solution()
  print a.hammingDis(3, 7)
