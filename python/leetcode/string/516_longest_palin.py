"""
516. Longest Palindromic Subsequence (Medium)

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
"""

"""
dp:
dp[i, j] := longest palindrome from i to j of substring s[i..j+1]

or bottom-up memoized dp?
"""

class Solution(object):
  def longestPalindromeSubseq(self, s):
    """
    :type s: str
    :rtype: int
    """
    stat = {}
    result = self.helper(s, stat, 0, len(s)-1)
    print stat
    return result

  def helper(self, s, stat, i, j):
    # not AC, TLE
    if i>j: return 0
    if (i,j) in stat:
      return stat[(i,j)]
    if i == j:
      stat[(i,j)] = 1
    elif i+1 == j:
      if s[i] == s[j]: stat[(i,j)] = 2
      else: stat[(i,j)] = 1
    else:
      # memoized dp
      # i not included
      if s[i] == s[j]:
        stat[(i,j)] = 2+self.helper(s, stat, i+1, j-1)
      else:
        stat[(i,j)] = max(self.helper(s, stat, i+1, j), self.helper(s,stat,i,j-1))
      '''result1 = self.helper(s, stat, i+1, j)
      # i included
      j_ = j
      while j_>i and s[j_]!=s[i]:
        j_ -= 1
      if j_>i:
        result2 = 2 + self.helper(s, stat, i+1, j_-1)
      else: result2 = 1
      stat[(i,j)] = max(result1, result2)'''
    print i,j,stat
    return stat[(i,j)]

  def solution2(self, s):
    # still no AC, TLE
    n = len(s)
    first = [1] * n
    second = [0] * n
    step = 1
    while len(first) > 1:
      result = []
      for i in range(n-step):
        if s[i] == s[i+step]: result.append(2+second[i+1])
        else: result.append(max(first[i], first[i+1]))
      first, second = result, first
      print first, second
      step += 1
    return first[0]

if __name__ == '__main__':
  a = Solution()
  # print a.longestPalindromeSubseq('bbbab')
  # print a.longestPalindromeSubseq('cbbd')
  # print a.longestPalindromeSubseq('aabaa')
  print a.solution2('bbbab')
  print a.solution2('cbbd')
  print a.solution2('aabaa')
