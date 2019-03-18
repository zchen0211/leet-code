"""
245. Shortest Word Distance III (Medium)

This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “makes”, word2 = “coding”, return 1.
Given word1 = "makes", word2 = "makes", return 3.

Note:
You may assume word1 and word2 are both in the list.
"""


class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        table = {}
        n = len(words)
        for i in range(n):
            word = words[i]
            if word in table:
                table[word].append(i)
            else:
                table[word] = [i]

        # case 1:
        if word1 != word2:
            n1, n2 = len(table[word1]), len(table[word2])
            best = max(table[word1]) + max(table[word2])
            i1, i2 = 0, 0
            while i1 < n1 and i2 < n2:
                id1_ = table[word1][i1]
                id2_ = table[word2][i2]
                best = min(best, abs(id1_ - id2_))
                if id1_ < id2_:
                    i1 += 1
                else:
                    i2 += 1
            return best
        else:
            n1 = len(table[word1])
            best = n
            for i in range(n1 - 1):
                best = min(best, table[word1][i + 1] - table[word1][i])
            return best
