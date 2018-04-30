'''
151. Reverse Words in a String (Medium)

Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.
'''

class Solution(object):
  def reverseWords(self, s):
    """
    :type s: str
    :rtype: str
    """
    result = s.split()
    result = result[::-1]
    result = ' '.join(result)
    return result


if __name__ == '__main__':
  a = Solution()
  print a.reverseWords("the sky is blue")
