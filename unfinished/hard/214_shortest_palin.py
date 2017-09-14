"""
214. Shortest Palindrome (Hard)

Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".
"""

class Solution(object):
  def solve(self, s):
    # brute-force: can pass
    n = len(s)
    if n == 0: return s

    rev = s[::-1]
    for i in range(n):
      if s.startswith(rev[i:]):
        return rev[:i] + s 

  def shortestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    n = len(s)
    c_odd = 0
    # longest odd palin
    i = (n-1)/2
    while i>=0:
      if self.palin_odd(s, i):
        c_odd = i
        break
      i -= 1
    print 'longest odd: ', s[:2*c_odd+1]
    # longest even palin
    c_even = 0
    i = (n-1)/2
    while i>=0:
      print 'i', i
      if self.palin_even(s, i):
        c_even = i
        break
      i -= 1
    print 'even: ', c_even
    if c_even == 0:
      if n<2 or s[0]!=s[1]: c_even = -1
    if c_even >=0:
      print 'longest even: ', s[:2*c_even+2]
    longest = max(2*c_odd+1, 2*c_even+2)
    tail = s[longest:]
    return tail[::-1]+s


  def palin_odd(self, s, center):
    i = center
    n = len(s)
    while i>=0 and 2*center-i<n:
      i -= 1
      if i>=0 and 2*center-i<n: # not out of boundary
        # still symmetric
        if s[i] != s[2*center-i]: return False
    return True

  def palin_even(self, s, left):
    i = left # left
    j = left+1 # right
    n = len(s)
    while i>=0 and j<n:
      print s[i], s[j]
      if s[i] != s[j]: return False
      i -= 1
      j += 1
    return True


if __name__ == '__main__':
  a = Solution()
  # print a.shortestPalindrome("aacecaaa")
  # print a.shortestPalindrome("abcd")
  print a.shortestPalindrome("abbacd")
  
