"""
678. Valid Parenthesis String (Medium)

Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
Note:
The string size will be in the range [1, 100].
"""

class Solution(object):
    def solve2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = 0
        i = 0
        n = len(s)
        cnt = 0
        while i < n:
            if s[i] == '(':
                cnt += 1
            elif s[i] == '*':
                stack += 1
            else: # ')'
                if cnt > 0:
                     cnt -= 1
                else:
                    if stack == 0:
                        return False
                    else:
                        stack -= 1
            i += 1
        # case 1:
        if cnt == 0: return True
        # reverse
        print 'round 1', cnt
        
        stack = 0
        i = n - 1
        cnt = 0
        while i >= 0:
            if s[i] == ')':
                cnt += 1
            elif s[i] == '*':
                stack += 1
            else:
                if cnt > 0:
                    cnt -= 1
                else:
                    if stack == 0:
                        return False
                    else:
                        stack -= 1
            i -= 1
        print 'round 2', cnt
        return True


if __name__ == "__main__":
    a = Solution()
    # print a.checkValidString("()")
    # print a.checkValidString("(*)")
    # print a.checkValidString("(*))")
    # print a.checkValidString(")(*))")
    print a.solve2("()")
    print a.solve2("(*)")
    print a.solve2("(*))")
    print a.solve2(")(*))")
    print a.solve2("((**")
    print a.solve2("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())")
    print a.solve2("(*()")
