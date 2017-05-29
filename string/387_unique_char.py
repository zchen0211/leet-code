'''
387. First Unique Character in a String (Easy)

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''

from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0: return -1
        
        stat = dict(Counter(s))
        for i in range(n):
            if stat[s[i]] == 1:
                return i
        return -1
