'''
301. Remove Invalid Parentheses (Hard)

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
'''

"""
For a better view see here

Key Points:

Generate unique answer once and only once, do not rely on Set.
Do not need preprocess.
Runtime 3 ms.
Explanation:
We all know how to check a string of parentheses is valid using a stack. Or even simpler use a counter.
The counter will increase when it is ‘(‘ and decrease when it is ‘)’. Whenever the counter is negative, we have more ‘)’ than ‘(‘ in the prefix.

To make the prefix valid, we need to remove a ‘)’. The problem is: which one? The answer is any one in the prefix. However, if we remove any one, we will generate duplicate results, for example: s = ()), we can remove s[1] or s[2] but the result is the same (). Thus, we restrict ourself to remove the first ) in a series of concecutive )s.

After the removal, the prefix is then valid. We then call the function recursively to solve the rest of the string. However, we need to keep another information: the last removal position. If we do not have this position, we will generate duplicate by removing two ‘)’ in two steps only with a different order.
For this, we keep tracking the last removal position and only remove ‘)’ after that.

Now one may ask. What about ‘(‘? What if s = ‘(()(()’ in which we need remove ‘(‘?
The answer is: do the same from right to left.
However a cleverer idea is: reverse the string and reuse the code!

Keypoints:
1. when stack < 0:
  i in [last_i, n-1] (because for "())())")
    j in [last_j, i] (because remove the duplicate of the same token twice)
      s[j-1] != par[1] ("))))" just remove the first one)
"""

class Solution(object):
  def solve2(self, s):
    ans = []
    self.remove(s, ans, 0, 0, ['(', ')'])
    return ans

  def remove(self, s, ans, last_i, last_j, par):
    stack = 0
    for i in range(last_i, len(s)):
      if s[i] == par[0]: stack += 1
      if s[i] == par[1]: stack -= 1
      if stack >= 0: continue
      for j in range(last_j, i+1):
        if s[j] == par[1] and (j==last_j or s[j-1]!=par[1]):
          self.remove(s[:j]+s[j+1:], ans, i, j, par)
      return
    s_rev = s[::-1]
    if par[0] == '(': # finished left to right
      self.remove(s_rev, ans, 0, 0, [')', '(']);
    else:
      ans.append(s_rev)

  def removeInvalidParentheses(self, s):
    """
    :type s: str
    :rtype: List[str]
    """
    result = [""]
    n = len(s)
    if n == 0: return result
    stat = []

    result = set()
    result.add("")
    i = 0
    while i < n:
      print i,
      if i == 0:
        if s[0] == '(': stat.append(1)
        else: stat.append(-1)
      else:
        if s[i] == '(': stat.append(stat[-1]+1)
        elif s[i] == ')': stat.append(stat[-1]-1)
        else: stat.append(stat[-1])
      
      new_result = set()
      for item in result:
        new_result.add(item+s[i])
      result = new_result
      
      print 'result before: ', result, len(result)
      # case 1: -1
      # remove any ) in result
      if stat[-1] == -1:
        new_result = set()
        for str_ in result:
          if str_ == "": new_result.add(str_)
          else:
            for j in range(len(str_)):
              if str_[j] == ')':
                print j
                new_result.add(str_[:j]+str_[j+1:])
        result = new_result
        stat = stat[:-1]
      print 'after: ', result, stat
      # if i == 3: break
      i += 1
    return list(result)
 
if __name__ == "__main__":
  a = Solution()
  # print a.removeInvalidParentheses("()())())")
  # print a.removeInvalidParentheses("(a)())()")

  # print a.solve2("()(")
  print a.solve2("()())())((")
