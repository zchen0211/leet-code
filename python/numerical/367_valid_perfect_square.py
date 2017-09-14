'''
367. Valid Perfect Square (Easy)

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False
'''

class Solution(object):
  def isPerfectSquare(self, num):
    if num == 0 or num == 1:
      return True
    elif num < 0:
      return False

    # bi-search
    st = 1
    end = num
    mid = (st + end) / 2
    while(st < end):
      print st, end
      if mid > num/mid:
        end = mid - 1
      elif mid < num/mid:
        st = mid + 1
      else: # mid close
        break     
      mid = (st + end) / 2
    if mid * mid == num or end * end == num:
      return True
    else:
      return False


if __name__ == '__main__':
  a = Solution()
  # for i in range(10):
  #   print i, a.isPerfectSquare(i)
  print a.isPerfectSquare(104976)
# 5 => 
