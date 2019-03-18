"""
21. Merge Two Sorted Lists (Easy)

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        tmp = head

        while l1 is not None or l2 is not None:
            if l2 is None or (l1 is not None and l1.val <= l2.val):
                if head is None:
                    head = l1
                    tmp = l1
                else:
                    tmp.next = l1
                    tmp = tmp.next
                l1 = l1.next
            else:
                if head is None:
                    head = l2
                    tmp = l2
                else:
                    tmp.next = l2
                    tmp = tmp.next
                l2 = l2.next
        return head
