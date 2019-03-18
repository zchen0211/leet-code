'''
306. Additive Number (Medium)

Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

For example:
"112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199
Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Follow up:
How would you handle overflow for very large input integers?
'''

"""
generate first and second;
all following goes recursively
"""

class Solution(object):
  def isAdditive(self, num):
    n = len(num)
    if n <= 2: return False
    for i in range(1, (n+1)/2):
      for j in range(1, (n+1)/2):
        # first
        first = int(num[0:i])
        if num[0] == '0' and i>1: continue
        # second
        second = int(num[i:i+j])
        # check
        if num[i] == '0' and j>1: continue
        ii, jj = i, j
        while(ii+jj<=n-1):
          third = str(first+second)
          k = len(third)
          if ii+jj+k>n:
            break
          if num[ii+jj:ii+jj+k] == third:
            first, second = second, int(third)
            if ii+jj+k == n:
              return True
            else:
               ii, jj = ii+jj, k
          else:
            break
          
    return False

if __name__ == '__main__':
  a = Solution()
  print a.isAdditive('112358')
  print a.isAdditive('199100199')
  print a.isAdditive('1357')
  print a.isAdditive('101')
  print a.isAdditive('0235813')
