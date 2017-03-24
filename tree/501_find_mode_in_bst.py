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
