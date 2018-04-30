"""
244. Shortest Word Distance II (Medium)

This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters. How would you optimize it?

Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = "coding", word2 = "practice", return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""

class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        n = len(words)
        self.table = {}
        for i in range(n):
          word = words[i]
          if word in self.table:
            self.table[word].append(i)
          else:
            self.table[word] = [i]


    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        print word1, self.table[word1]
        print word2, self.table[word2]
        n1, n2 = len(self.table[word1]), len(self.table[word2]) 
        best = max(self.table[word1]) + max(self.table[word2])
        i1, i2 = 0, 0
        while i1 < n1 and i2 < n2:
          id1_ = self.table[word1][i1]
          id2_ = self.table[word2][i2]
          best = min(best, abs(id1_ - id2_))
          print id1_, id2_, best
          if id1_ < id2_: i1 += 1
          else: i2 += 1
        return best

if __name__ == "__main__":
  cls = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
  print cls.shortest("coding","practice")

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
