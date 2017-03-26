# def guess(num):


class Solution(object):
  def guessNumber(self, n):
    low, high = 1, n
    mid = (low+high)/2 
    while(high!=low):
      if guess(mid) == -1:
        low = mid + 1
      elif guess(mid) == 0:
        return mid
      else:
        high = mid-1

