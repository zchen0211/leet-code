'''
605. Can Place Flowers (Easy)

Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.
'''

class Solution(object):
  def canPlaceFlowers(self, flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    if n <= 0: return True
    n_f = len(flowerbed)
    if n > n_f: return False
    if n_f == 1:
      if flowerbed[0] == 0: return True
      else: return False
    cnt = 0
    for i in range(n_f):
      if flowerbed[i] == 0:
        if i == 0 and flowerbed[i+1] == 0:
          flowerbed[i] = 1
          cnt += 1
        elif i == n_f-1 and flowerbed[i-1] == 0:
          flowerbed[i] = 1
          cnt += 1
        elif flowerbed[i-1]==0 and flowerbed[i+1]==0:
          flowerbed[i] = 1
          cnt += 1
      if cnt >= n: return True
    return False


if __name__ == '__main__':
  a = Solution()
  print a.canPlaceFlowers([1,0,0,0,1], 1)
  print a.canPlaceFlowers([1,0,0,0,1], 2)
