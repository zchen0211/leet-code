class Solution(object):
  def validAbbr(self, s, abbr):
    si = 0
    abbr_i = 0
    while(abbr_i<len(abbr) and si<len(s)):
      if abbr[abbr_i]<'0' or abbr[abbr_i]>'9':
        if si>=len(s) or abbr[abbr_i] != s[si]:
          return False
        else:
          si += 1
          abbr_i += 1
      else:
        cnt = 0
        while(abbr_i<len(abbr) and abbr[abbr_i]>='0' and abbr[abbr_i]<='9'):
          cnt = cnt*10 + int(abbr[abbr_i])
          abbr_i += 1
        si += cnt
    if si==len(s) and abbr_i==len(abbr):
      return True
    else:
      return False


if __name__ == '__main__':
  a = Solution()
  print a.validAbbr('abcd', '5')
  print a.validAbbr("internationalization", "i12iz4n")
