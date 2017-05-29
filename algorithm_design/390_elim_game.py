'''
390. Elimination Game (Medium)

There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Find the last number that remains starting with a list of length n.

Example:

Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output:
6
'''

class Solution(object):
  def lastRemaining(self, n):
    """
    :type n: int
    :rtype: int
    """
    flag = True # remove from left
    min_, max_ = 1, n
    interval = 1

    # cnt = 0
    while(min_<max_):
      if flag:
        if (max_-min_)/interval % 2 == 0:
          max_ = max_ - interval
        min_ = min_ + interval
      else:
        if (max_-min_)/interval % 2 == 0:
          min_ += interval
        max_ = max_ - interval
      interval *= 2
      flag = not flag
      # cnt += 1
    return min_

if __name__ == '__main__':
  a = Solution()
  print a.lastRemaining(100)
