'''
20. Valid Parentheses (Easy)

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            else:
                if stack and mapping[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
