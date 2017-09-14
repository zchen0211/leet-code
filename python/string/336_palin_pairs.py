"""
336. Palindrome Pairs (Hard)

Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
"""

class Trie():
  def __init__(self):
    self.maps = {}
    self.is_word = False
    # self.ids = []
    self.id_ = -1

class Solution(object):
  def palindromePairs(self, words):
    """
    :type words: List[str]
    :rtype: List[List[int]]
    """
    # add every word into a Trie
    root = Trie()
    for ii in range(len(words)):
      word = words[ii]
      node = root
      if word == '':
        node.is_word = True
        # node.ids.append(ii)
        node.id_ = ii
      for i in range(len(word)):
        c = word[i]
        if c not in node.maps:
          node.maps[c] = Trie()
        # node.ids.append(ii)
        node = node.maps[c]
        if i == len(word)-1: # last character
          node.is_word = True
          # node.ids.append(ii)
          node.id_ = ii
    result = []

    def traverse(node, prefix, ii):
      if node.is_word and self.is_palin(prefix) and node.id_!=ii:
        result.append([node.id_, ii])
      for c in node.maps:
        traverse(node.maps[c], prefix+c, ii)

    for ii in range(len(words)):
      word = words[ii]
      word = word[::-1]
      node = root
      if root.is_word:
        if self.is_palin(word) and ii != node.id_:
          # print word, ii
          result.append([node.id_, ii])
          # print result
          result.append([ii, node.id_])
          # print result
      # look up first
      for i in range(len(word)):
        c = word[i]
        if c not in node.maps: break
        node = node.maps[c]
        if node.is_word: # is_word
          # check word[i+1..]
          tmp = word[i+1:]
          if self.is_palin(tmp) and ii != node.id_:
            result.append([node.id_, ii])
        if i == len(word)-1:
          # traverse
          traverse(node, '', ii)
          '''
          for idx in node.ids:
            if self.is_palin(words[idx][i+1:]) and ii != idx:
              result.append([idx, ii])
          '''

    print result
    result = set([tuple(item) for item in result])
    result = list(result)
    result = [list(item) for item in result]
    return result

  def is_palin(self, word):
    i = 0
    j = len(word) - 1
    while i < j and word[i] == word[j]:
      i += 1
      j -= 1
    if i >= j: return True
    else: return False


if __name__ == "__main__":
  a = Solution()
  print a.palindromePairs(["ba", "abc"])
  print a.palindromePairs(["bat", "tab", "cat"])
  print a.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"])
  print a.palindromePairs(["a", "", "aa"])
  print a.palindromePairs(["a","b","c","ab","ac","aa"])
  print a.palindromePairs(["a","ab","ac"])
