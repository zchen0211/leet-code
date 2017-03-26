class Solution(object):
  def reverseVowels(self, s):
    v_set = set(['a','e','i','o','u','A','E','I','O','U'])
    i = 0
    j = len(s) - 1
    s = list(s)
    while(i<j):
      while(i<j and s[i] not in v_set):
        i += 1
      while(j>i and s[j] not in v_set):
        j -= 1
      # swap i, j
      s[i], s[j] = s[j], s[i]
      i += 1
      j -= 1
    return ''.join(s)


if __name__ == '__main__':
  a = Solution()
  print a.reverseVowels('leetcode')
