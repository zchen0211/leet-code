'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
'''


class Solution(object):
  def wordPattern(self, pattern, strs):
    strs_list = strs.split()
    if len(pattern) != len(strs_list):
      return False
    hash_p2s = {}
    hash_s2p = {}
    for i in range(len(pattern)):
      p = pattern[i]
      s = strs_list[i]
 
      if not hash_p2s.has_key(p):
        hash_p2s[p] = s
      else:
        if hash_p2s[p] != s:
          return False
      if not hash_s2p.has_key(s):
        hash_s2p[s] = p
      else:
        if hash_s2p[s] != p:
          return False
    return True


if __name__ == '__main__':
  a = Solution()
  print a.wordPattern('abba', 'dog cat cat dog')
