'''
385. Mini Parser (Medium)

Given a nested list of integers represented as a string, implement a parser to deserialize it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Note: You may assume that the string is well-formed:

String is non-empty.
String does not contain white spaces.
String contains only digits '0-9' , '[' , '-' , ',' , ']'.
Example 1:

Given s = "324",

You should return a NestedInteger object which contains a single integer 324.

Example 2:

Given s = "[123,[456,[789]]]",

Return a NestedInteger object containing a nested list with 2 elements:

1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789.
'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
  def deserialize(self, s):
    """
    :type s: str
    :rtype: NestedInteger
    """
    d_set = set(['-','0','1','2','3','4','5','6','7','8','9'])
    n = len(s)
    stack = []
    i = 0
    if s[0] in d_set:
      result = int(s)
    else:
      while(i<n):
        if s[i] == '[':
          i += 1 
          tmp = []
          # put all numbers in tmp until next '[' or ']'
          j = i + 1
          while(s[j]!='[' and s[j]!=']'):
            if s[j] in d_set: j += 1
            else: # ','
               tmp.append(int(s[i:j]))
  
  def str_2_list(self, s): # divide and conquer
    assert s[0] == '['
    assert s[-1] == ']'
    result = []
    start_nest_id = None
    d_set = set(['-','0','1','2','3','4','5','6','7','8','9'])
    # start part until '['
    i = 1
    n = len(s)
    while(i<n and s[i]!='[' and s[i]!=']'):
      if s[i] in d_set:
        j = i+1
        while(s[j] in d_set):
          j = j+1
        result.append(int(s[i:j]))
      i = j+1
    if s[i]<n and s[i]=='[':
      # append a middle result
      pass
    return result


if __name__ == '__main__':
  a = Solution()
  print a.str_2_list('[1,2,33]')
