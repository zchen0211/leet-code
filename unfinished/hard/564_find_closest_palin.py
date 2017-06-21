'''
564. Find the Closest Palindrome (Hard)

Given an integer n, find the closest integer (not including itself), which is a palindrome.

The 'closest' is defined as absolute difference minimized between two integers.

Example 1:
Input: "123"
Output: "121"
Note:
The input n is a positive integer represented by string, whose length will not exceed 18.
If there is a tie, return the smaller one as answer.
'''

class Solution(object):
  def nearestPalindromic(self, n):
    """
    :type n: str
    :rtype: str
    """
    if n == '0': return '1'
    if len(n) == 1:
      return str(int(n)-1)

    n_list = []
    for i in range(len(n)): n_list.append(n[i])
    n_list = [int(item) for item in n_list]

  def isPalin(self, s):
    i = 0
    j = len(s)-1
    while i<j:
      if s[i] == s[i]:
        i, j = i+1, j-1
      else: return False
    return True

  def helper_smaller(self, s):
    n = len(s)
    if self.isPalin(s):
      # decrese the first non-zero near center symmetrically
      if n % 2 == 1:
        i, j = (n-1)/2
      else:
        i, j = n/2-1, n/2
      while i>=0:
        if s[i] > 0:
          s[i], s[j] = s[i]-1, s[j]-1 
          break
        i, j = i-1, j+1
      # if not 100001
      if sum(s) != 0: return s
      else: return [9]*(n-1)
    else:
      # first difference take smaller
      i = 0
      j = n-1
      # center '99999'
      while 

  def helper_larger(self, s):
    if self.isPalin(s):
      # increase the first non-9 digit symmetrically
      # if all 9, 100001
    else: # not palin
      # first difference take larger
      # all center '00000'

if __name__ == '__main__':
  a = Solution()
  print a.nearestPalindromic('12345')
