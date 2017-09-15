'''
14. Longest Common Prefix (Easy)

Write a function to find the longest common prefix string amongst an array of strings.
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        if n == 0: return ""
        if n == 1: return strs[0]
        
        result = ""
        max_ = min([len(item) for item in strs])
        i = 0
        while i < max_:
            c = strs[0][i]
            for j in range(1, n):
                if strs[j][i] != c:
                    return result
            result += c
            i += 1
        return result

