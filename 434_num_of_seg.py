class Solution(object):
  def countSeg(self, s):
    cnt = 0
    if len(s) == 0:
      return cnt
    i = 0
    Flag = True
    while(i<len(s)):
      if s[i] != ' ' and Flag:
        cnt += 1
        Flag = False
      elif s[i] == ' ':
        Flag = True
      i += 1
    return cnt


if __name__ == '__main__':
  a = Solution()
  print a.countSeg("Hello, my name is John")
