"""
2. Add Two Numbers (Medium)

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        tmp_l1 = l1
        tmp_l2 = l2
        l3_head = None
        tmp_l3_last = l3_head
        carry_flag = False
        while tmp_l1 is not None or tmp_l2 is not None:
            # create a new node
            if tmp_l1 is not None and tmp_l2 is not None:
                tmp_l3 = ListNode(tmp_l1.val + tmp_l2.val)
            elif tmp_l1 is not None:
                tmp_l3 = ListNode(tmp_l1.val)
            else:
                tmp_l3 = ListNode(tmp_l2.val)
            if carry_flag:
                tmp_l3.val += 1
            if tmp_l3.val >= 10:
                carry_flag = True
                tmp_l3.val -= 10
            else:
                carry_flag = False

            # append
            if tmp_l3_last is None:  # head
                l3_head = tmp_l3
            else:
                tmp_l3_last.next = tmp_l3
            tmp_l3_last = tmp_l3
            # move forward
            if tmp_l1:
                tmp_l1 = tmp_l1.next
            if tmp_l2:
                tmp_l2 = tmp_l2.next
        # append the last 1 if necessary
        if carry_flag:
            tmp_l3 = ListNode(1)
            tmp_l3_last.next = tmp_l3
        return l3_head
