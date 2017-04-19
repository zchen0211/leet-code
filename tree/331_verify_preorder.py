'''
One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

Example 1:
"9,3,4,#,#,1,#,#,2,#,6,#,#"
Return true

Example 2:
"1,#"
Return false

Example 3:
"9,#,#,1"
Return false
'''

class Solution(object):
  def isValid(self, preorder):
    pre_list = preorder.split(',')
    n = len(pre_list)
    if pre_list[0] == '#':
      return n==1
    node_list = [pre_list[0]]
    visit_list = [0]

    for i in range(1, n):
      if pre_list[i] != '#':
        node_list.append(pre_list[i])
        visit_list.append(0)
      else:
        visit_list[-1] += 1
        while(visit_list and visit_list[-1]==2):
          visit_list.pop()
          node_list.pop()
          if visit_list:
            visit_list[-1] += 1
        if not visit_list and i!=n-1: return False
      print node_list, visit_list
    return not visit_list


if __name__ == '__main__':
  a = Solution()
  # print a.isValid("9,3,4,#,#,1,#,#,2,#,6,#,#")
  # print a.isValid('1,#')
  print a.isValid('1,#,#,2')
