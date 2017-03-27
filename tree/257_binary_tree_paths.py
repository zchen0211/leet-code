'''
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        # if leaf node
        if root.left is None and root.right is None:
            return [str(root.val)]
        else:
            result = []
            if root.left:
                result_l = self.binaryTreePaths(root.left)
                result += [str(root.val)+'->'+item for item in result_l]
            if root.right:
                result_r = self.binaryTreePaths(root.right)
                result += [str(root.val)+'->'+item for item in result_r]
        return result
