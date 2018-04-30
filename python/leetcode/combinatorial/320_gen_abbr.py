"""
320. Generalized Abbreviation (Medium)

Write a function to generate the generalized abbreviations of a word.

Example:
Given word = "word", return the following list (order does not matter):
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
"""

class Solution(object):
  def generateAbbreviations(self, word):
    """
    :type word: str
    :rtype: List[str]
    """
    ret = self.helper(word)
    # print ret
    ret2 = []
    for list_ in ret:
      res = ""
      for item in list_:
        if isinstance(item, int):
          res += str(item)
        else:
          res += item
      ret2.append(res)
    return ret2

  def helper(self, word):
    n = len(word)
    # print word, n
    if n == 0: return [""]
    if n == 1:
      ret = [[1], [word]]
      return ret

    word1, word2 = word[:n/2], word[n/2:]
    ret1 = self.helper(word1)
    ret2 = self.helper(word2)
    ret = []
    for list1 in ret1:
      for list2 in ret2:
        tmp_list = [item for item in list1]
        if isinstance(list1[-1], int) and isinstance(list2[0], int):
          tmp_list[-1] += list2[0]
          for item in list2[1:]:
            tmp_list.append(item)
        else:
          for item in list2:
            tmp_list.append(item)
        ret.append(tmp_list)
    return ret


if __name__ == "__main__":
  a = Solution()
  print len(a.generateAbbreviations("word"))
