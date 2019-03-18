"""
606. Construct String from Binary Tree (Easy)

You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())", 
but you need to omit all the unnecessary empty parenthesis pairs. 
And it will be "1(2(4))(3)".

Example 2:
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example, 
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def tree2str(self, t):
        """
    :type t: TreeNode
    :rtype: str
    """
        if t is None:
            return ""
        result = self.helper(t)
        return result

    def helper(self, t):
        result = ""
        result += str(t.val)
        if t.left is None and t.right is None:
            return result

        if t.left is not None:
            result += "(" + self.helper(t.left) + ")"
        else:
            result += "()"

        if t.right is not None:
            result += "(" + self.helper(t.right) + ")"
        return result


if __name__ == "__main__":
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t1.left, t1.right = t2, t3
    t2.left = t4

    a = Solution()
    a.tree2str(t1)
