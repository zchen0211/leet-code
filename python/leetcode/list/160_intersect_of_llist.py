"""
160. Intersection of Two Linked Lists (Easy)

Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""

"""
Solution:
1. easy way: keep a hash table;
  problem: O(n) time, O(n) memory;
2. imagine the list as:
    a-self->
             ab-shared
    b-self->
  pointer A goes a-self, ab-shared, b-self
  pointer B goes b-self, ab-shared, a-self
  A and B will meet at the intersection point;
  if A and B doesn't meet, A == B will end at None;
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        tmp1 = headA
        tmp2 = headB
        while tmp1 != tmp2:
            if tmp1 is not None:
                tmp1 = tmp1.next
            else:
                tmp1 = headB
            if tmp2 is not None:
                tmp2 = tmp2.next
            else:
                tmp2 = headA
        return tmp1
