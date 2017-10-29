"""
249. Group Shifted Strings (Medium)

Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], 
A solution is:

[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
"""

class Solution(object):
  def groupStrings(self, strings):
    """
    :type strings: List[str]
    :rtype: List[List[str]]
    """
    self.table = {}

    for item in strings:
      curr = []
      # encode
      for c in item:
        curr.append(ord(c) - ord('a'))
      # shift
      offset = curr[0]
      curr = [(enc-offset)%26 for enc in curr]
      curr = tuple(curr)

      if curr in self.table:
        self.table[curr].append(item)
      else:
        self.table[curr] = [item]

    res = []
    for k in self.table:
      res.append(self.table[k])
    return res

if __name__ == "__main__":
  a = Solution()
  print a.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])

