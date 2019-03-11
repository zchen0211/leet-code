"""
1008. Construct Binary Search Tree from Preorder Traversal (Medium)

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Note: 

1 <= preorder.length <= 100
The values of preorder are distinct.
"""

"""
Idea: recursive
for a subarray:
  1st item: root
  all items < 1st: left child
  all items > 1st: right child
empty array: None
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        left_pre = []
        i = 1
        while i < len(preorder) and preorder[i] < root.val:
            left_pre.append(preorder[i])
            i += 1
        right_pre = preorder[i:]
        root.left = self.bstFromPreorder(left_pre)
        root.right = self.bstFromPreorder(right_pre)
        return root


if __name__ == "__main__":
    a = Solution()
    print(a.bstFromPreorder([8,5,1,7,10,12]))

