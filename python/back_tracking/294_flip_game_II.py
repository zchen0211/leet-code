"""
294. Flip Game II (Medium)

You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

For example, given s = "++++", return true. The starting player can guarantee a win by flipping the middle "++" to become "+--+".

Follow up:
Derive your algorithm's runtime complexity.
"""

class Solution(object):
  def solve(self, s):
    if len(s) < 2: return False

    n = len(s)
    for i in range(n-1):
      if s[i:i+2] == "++":
        t = s[:i] + "--" + s[i+2:]
        if not self.solve(t):
          return True
    return False

  def solve2(self, s):
    self.memo = {}
    ret = self.helper(s)
    print self.memo
    return ret 

  def helper(self, s):
    n = len(s)
    if s not in self.memo:
      for i in range(n-1):
        if s[i:i+2] == "++":
          t = s[:i] + "--" + s[i+2:]
          if not self.helper(t):
            self.memo[s] = True
            return True
      self.memo[s] = False
    return self.memo[s]

  def canWin(self, s):
    """
    :type s: str
    :rtype: bool
    """
    curlen = 0
    maxlen = 0

    # board representation
    board = []
    for i in range(len(s)):
      if s[i] == '+':
        curlen += 1
      if i == len(s) - 1 or s[i] == '-':
        if curlen >= 2:
          board.append(curlen)
        maxlen = max(maxlen, curlen)
        curlen = 0

    # Sprague-Grundy function
    g = [0] * (maxlen + 1)
    for len_ in range(2, maxlen + 1):
      gsub = set()
      for len_first in range(0, len_/2):
        len_second = len_ - len_first - 2
        gsub.add(g[len_first] ^ g[len_second])
      print len_, gsub
      g[len_] = self.mex(gsub)
    print g

    # xor of all sub-games
    g_final = 0
    for item in board:
      g_final = g_final ^ g[item]
    return g_final != 0


  def mex(self, lut):
    m = len(lut)
    for i in range(m):
      if i not in lut:
        return i
    return m


if __name__ == "__main__":
  a = Solution()
  print a.canWin("+++++")
  print a.solve("+++++")
  print a.solve2("+++++")
