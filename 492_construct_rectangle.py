import math


class Solution(object):
  def constructRectangle(self, area):
    if area == 0:
      return [0, 0]
    elif area == 1:
      return [1, 1]
    x = int(math.floor(math.sqrt(area)))
    while(x>=1):
      if area % x == 0:
        return [area/x, x]
      else:
        x -= 1


if __name__ == '__main__':
  a = Solution()
  print a.constructRectangle(5)
