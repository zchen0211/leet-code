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

"""
The problem wants us to find the number of ways to do something without giving specific steps like how to achieve it. This can be a typical signal that dynamic programming may come to help.

dp[i][j] stands for the minimal turns we need for string from index i to index j.
So we have

dp[i][i] = 1: we need 1 turn to paint a single character.
dp[i][i + 1]
dp[i][i + 1] = 1 if s.chartAt(i) == s.charAt(i + 1)
dp[i][i + 1] = 2 if s.chartAt(i) != s.charAt(i + 1)
Then we can iteration len from 2 to possibly n. For each iteration, we iteration start index from 0 to the farthest possible.

The maximum turns for dp[start][start + len] is len + 1, i.e. print one character each time.
We can further divide the substring to two parts: start -> start+k and start+k+1 -> start+len. It is something as following:
index |start  ...  start + k| |start + k + 1 ... start + len|
char  |  a    ...       b   | |      c       ...      b     |
As shown above, if we have s.charAt(start + k) == s.charAt(start + len), we can make it in one turn when we print this character (i.e. b here)
This case we can reduce our turns to dp[start][start + k] + dp[start + k + 1][start + len] - 1
Complete codes are here
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
