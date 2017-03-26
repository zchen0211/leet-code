import collections


class Solution(object):
  def canConstruct(self, ransomNote, magazine):
    result = collections.Counter(ransomNote) - collections.Counter(magazine)
    return not result


if __name__ == '__main__':
  a = Solution()
  print a.canConstruct('aa', 'aab')
