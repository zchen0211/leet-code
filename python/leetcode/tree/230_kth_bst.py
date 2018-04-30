'''
230. Kth Smallest Element in a BST (Medium)

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 <= k <= BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # AC: original solution
        record = []
        stack = [root]
        visit = set([root])
        while(len(record)<k and stack):
            if stack[-1].left is not None and stack[-1].left not in visit:
                visit.add(stack[-1].left)
                stack.append(stack[-1].left)
            else:
                n = stack.pop()
                record.append(n.val)
                if n.right is not None:
                    visit.add(n.right)
                    stack.append(n.right)
            print len(stack), record
        return record[k-1]

    def solution2(self, root, k):
      # AC: shorter, same time
      # in-order iteratively without a "visit set"
      stack = [root]
      while stack[-1].left is not None:
        stack.append(stack[-1].left)

      while(k>0):
        tmp = stack.pop()
        k -= 1
        if k == 0: return tmp.val
        if tmp.right:
          stack.append(tmp.right)
          while(stack[-1].left is not None):
            stack.append(stack[-1].left)

if __name__ == '__main__':
  a = Solution()
  node1 = TreeNode(2)
  node2 = TreeNode(1)
  node1.left = node2
  print a.kthSmallest(node1, 2)
  print a.solution2(node1, 2)
