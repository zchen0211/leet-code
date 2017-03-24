class Solution(object):
  def findContentChildren(self, g, s):
    g.sort()
    s.sort()
    cnt = 0
    gi = 0
    si = 0
    while(gi<len(g) and si<len(s)):
      if g[gi] <= s[si]: # satisified
        cnt += 1
        gi += 1
        si += 1
      else:
        si += 1
    return cnt


if __name__ == '__main__':
  a = Solution()
  print a.findContentChildren([1,2], [1,2,3])
