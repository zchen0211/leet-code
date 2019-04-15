# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        best, min_, max_ = self.helper(root)
        return best

    def helper(self, root):
        # corner case
        best, min_, max_ = 0, root.val, root.val
        b1, min1, max1 = None, None, None
        b2, min2, max2 = None, None, None
        if root.left is None and root.right is None:
            return 0, root.val, root.val
        if root.left is not None:
            b1, min1, max1 = self.helper(root.left)
            best = max(b1, max(max_, max1) - min(min_, min1))
            # min_ = min(min1, min_)
            # max_ = max(max1, max_)
        if root.right is not None:
            b2, min2, max2 = self.helper(root.right)
            best = max(b2, max(max_, max2) - min(min_, min2))
            
        if b1 is not None:
        	min_, max_ = min(min_, min1), max(max_, max1)
        if b2 is not None:
        	min_, max_ = min(min_, min2), max(max_, max2)

        return best, min_, max_