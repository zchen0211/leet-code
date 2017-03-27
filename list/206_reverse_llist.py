'''
Reverse a singly linked list.

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        newHead = head
        while(head.next is not None):
            # remove head next
            tmp = head.next
            head.next = tmp.next
            # insert in the beginning
            tmp.next = newHead
            # update newHead
            newHead = tmp
        # return newHead
        return newHead
