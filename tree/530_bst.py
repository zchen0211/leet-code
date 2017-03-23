# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        mylist = []
        self.InorderTraverse(root, mylist)
        print mylist
        tmp_val = mylist[1] - mylist[0]
        for i in range(1, len(mylist)):
            tmp_val = min(tmp_val, mylist[i]-mylist[i-1])
        return tmp_val
        
    def InorderTraverse(self, root, tmplist):
        if root is None:
            return
        else:
            self.InorderTraverse(root.left, tmplist)
            tmplist.append(root.val)
            self.InorderTraverse(root.right, tmplist)
