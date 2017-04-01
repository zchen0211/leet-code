'''
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.
'''

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution(object):
  def deleteNode(self, node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    if not node:
      return
    if node.next is None:  # actually this will do nothing
      node = None
    else:
      while(node.next):
        node.val = node.next.val
        if node.next.next is None:
          node.next = None
        else:
          node = node.next
    return

if __name__ == '__main__':
  node1 = ListNode(1)
  node2 = ListNode(2)
  node3 = ListNode(3)
  node4 = ListNode(4)
  node1.next = node2
  node2.next = node3
  node3.next = node4

  a = Solution()
  a.deleteNode(node4)
  node = node1
  while(node):
    print node.val
    node = node.next
