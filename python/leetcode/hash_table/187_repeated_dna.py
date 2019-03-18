"""
187 Repeated DNA Sequences (Medium)

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
"""


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        tmp_set = {}
        for i in range(n - 9):
            if tmp_set.has_key(s[i : i + 10]):
                tmp_set[s[i : i + 10]] += 1
            else:
                tmp_set[s[i : i + 10]] = 1
        # print tmp_set
        result = [k for k, v in tmp_set.items() if v > 1]
        return result
