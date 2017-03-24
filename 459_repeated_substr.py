class Solution(object):
  def repeatedSubstr(self, s):
    rep_s = (s + s)[1:-1]
    if rep_s.find(s) != -1:
      return True
    else:
      return False


if __name__ == '__main__':
  a = Solution()
  print a.repeatedSubstr('ababc')
