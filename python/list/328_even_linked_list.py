'''
328. Odd Even Linked List (Medium)

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...
'''

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None


class Solution(object):
  def oddEvenList(self, head):
    if head is None or head.next is None: return head

    odd_head = head
    odd_tail = head
    even_head = head.next
    even_tail = head.next
    
    tmp = even_head.next
    cnt = 1
    while(tmp is not None):
      if cnt % 2 == 1: # odd, add to odd_tail
        odd_tail.next = tmp
        odd_tail = odd_tail.next
      else: # even, add to even_tail
        even_tail.next = tmp
        even_tail = even_tail.next
      tmp_next = tmp.next
      tmp.next = None
      tmp = tmp_next
      cnt += 1
    odd_tail.next = even_head
    even_tail.next = None
    return odd_head


if __name__ == '__main__':
  a = Solution()
  l1 = ListNode(1)
  l2 = ListNode(2)
  l3 = ListNode(3)
  l4 = ListNode(4)
  l5 = ListNode(5)
  l1.next = l2
  l2.next = l3
  l3.next = l4
  # l4.next = l5
  head = a.oddEvenList(l1)
  tmp = head
  while(tmp is not None):
    print tmp.val
    tmp = tmp.next
