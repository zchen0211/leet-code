"""
49. Group Anagrams (Medium)

Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # notice! sort() modifies an array in place
        # it returns None
        mapping = {}
        for str_ in strs:
            re = list(str_)
            re.sort()
            re = "".join(re)
            if re in mapping:
                mapping[re].append(str_)
            else:
                mapping[re] = [str_]
        result = []
        for k in mapping.keys():
            tmp = list(mapping[k])
            result.append(tmp)
        return result
