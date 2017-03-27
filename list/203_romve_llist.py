'''
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
  def removeElements(self, head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    if head is None:
      return None
    # newHead
    newHead = head
    while(newHead is not None and newHead.val == val):
      newHead = newHead.next
    if newHead is None:
      return None
    tmp = newHead
    while(tmp.next is not None):
      if tmp.next.val == val:
        tmp.next = tmp.next.next
      else:
        tmp = tmp.next
    return newHead

  def Solution2(self, head, val):

  def Helper(self, head, curr, val):
    if curr is None:
      return head
    elif curr.val == val


if __name__ == '__main__':
  n1 = ListNode(1)
  n2 = ListNode(2)
  n3 = ListNode(1)
  n1.next = n2
  n2.next = n3

  a = Solution()
  x = a.removeElements(n1, 1)
  print x.val
  print x.next
