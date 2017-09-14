'''
301. Remove Invalid Parentheses (Hard)

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
'''

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
