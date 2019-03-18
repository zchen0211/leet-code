"""
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findMode(self, root):
        """
    :type root: TreeNode
    :rtype: List[int]
    """
        if root is None:
            return []
        # DFS
        in_order_list = []
        self.HelperFunc(root, in_order_list)
        # go through and keep record
        result_dic = {}
        for item in in_order_list:
            if result_dic.has_key(item):
                result_dic[item] += 1
            else:
                result_dic[item] = 1
        mode_cnt = max(result_dic.values())
        result = []
        for k, v in result_dic.items():
            if v == mode_cnt:
                result.append(k)
        return result

    def HelperFunc(self, root, in_order_list):
        # return (min_val, times) in root
        # return (max_val, times) in root
        # return best_result
        # collect (root_val, times)
        if root is None:
            return
        else:
            self.HelperFunc(root.left, in_order_list)
            in_order_list.append(root.val)
            self.HelperFunc(root.right, in_order_list)
