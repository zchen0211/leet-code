"""
664. Strange Printer (Hard)

There is a strange printer with the following two special requirements:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any places, and will cover the original existing characters.
Given a string consists of lower English letters only, your job is to count the minimum number of turns the printer needed in order to print it.

Example 1:
Input: "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".
Example 2:
Input: "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
Hint: Length of the given string will not exceed 100.
"""

class Solution(object):
  def strangePrinter(self, s):
    """
    :type s: str
    :rtype: int
    """
    n = len(s)
    if n == 0: return 0

    # dp[i..j] best result to get s[i..j]
    dp = [] # n x n [0] matrix
    for i in range(n):
      dp.append([1]*n)

    for i in range(1, n): # length will be i+1
      for j in range(n-i):
        dp[j][j+i] = i+1
        for k in range(j, j+i):
          tmp = dp[j][k] + dp[k+1][i+j]
          if s[k] == s[i+j]: tmp-=1
          dp[j][j+i] = min(dp[j][j+i], tmp)
    print dp
    return dp[0][-1]


if __name__ == "__main__":
  a = Solution()
  # print a.strangePrinter("aaabbb")
  print a.strangePrinter("moiulcxajmhtxipdymndmvezgitoddbbapjhsyrkduimlxhcamfpdxaqqxdbmrfmrmdsdgeravgzxwpczgfhbxidembvwehtqlvo")
  # print a.strangePrinter("aba")
