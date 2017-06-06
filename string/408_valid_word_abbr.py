'''
LeetCode 408. Valid Word Abbreviation (Easy)

Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.

A string such as "word" contains only the following valid abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
Notice that only the above abbreviations are valid abbreviations of the string "word". Any other string is not a valid abbreviation of "word".

Note:
Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

Example 1:

Given s = "internationalization", abbr = "i12iz4n":

Return true.

Example 2:

Given s = "apple", abbr = "a2e":

Return false.
'''

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
