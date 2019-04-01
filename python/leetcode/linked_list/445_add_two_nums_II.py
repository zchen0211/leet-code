"""
445. Add Two Numbers II (Medium)

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
        l_list1 = self.helper(l1)
        l_list2 = self.helper(l2)
        l_list1 = l_list1[::-1]
        l_list2 = l_list2[::-1]
        carry = False
        n_l1 = len(l_list1)
        n_l2 = len(l_list2)
        l_list3 = []
        for i in range(max(n_l1, n_l2)):
            if i < n_l1 and i < n_l2:
                tmp_sum = n_l1[i] + n_l2[i]
            elif i < n_l1:
                tmp_sum = n_l1[i]
            elif i < n_l2:
                tmp_sum = n_l2[i]
            if carry:
                tmp_sum += 1
            if tmp_sum >= 10:
                tmp_sum -= 10
                carry = True
            else:
                carry = False
            l_list3.append(tmp_sum)
        if carry:
            l_list3.append(1)
        l_list3 = l_list3[::-1]
        head = ListNode(l_list3[0])
        tmp = head
        for i in range(1, len(l_list3)):
            tmp1 = ListNode(l_list3[i])
            tmp.next = tmp1
            tmp = tmp.next
        return head

    def helper(self, l):
        l_list = []
        tmp = l
        while tmp is not None:
            l_list.append(tmp.val)
            tmp = tmp.next
        return l_list
