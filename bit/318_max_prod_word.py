'''
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.
'''

class Solution(object):
  def maxProduct(self, words):
    num = len(words)
    if num <= 1: return 0
    record = []
    for word in words:
      tmp_set = set(word)
      tmp_rec = 0
      j = 1
      for c in range(ord('a'), ord('z')+1):
        if chr(c) in tmp_set:
          tmp_rec = tmp_rec|j
        j = j<<1
      record.append(tmp_rec)
    # print record
    result = 0
    for i in range(num):
      for j in range(i+1, num):
        if record[i] & record[j] == 0:
          result = max(result, len(words[i])*len(words[j]))
    return result


if __name__ == '__main__':
  a = Solution()
  print a.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"])
  print a.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"])
