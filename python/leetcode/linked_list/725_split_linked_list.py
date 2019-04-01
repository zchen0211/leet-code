"""
725. Split Linked List in Parts (Medium)

Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive linked list "parts".

The length of each part should be as equal as possible: no two parts should have a size differing by more than 1. This may lead to some parts being null.

The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.

Return a List of ListNode's representing the linked list parts that are formed.

Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]
Example 1:
Input: 
root = [1, 2, 3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The input and each element of the output are ListNodes, not arrays.
For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3, and root.next.next.next = null.
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but it's string representation as a ListNode is [].
Example 2:
Input: 
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
Note:

The length of root will be in the range [0, 1000].
Each value of a node in the input will be an integer in the range [0, 999].
k will be an integer in the range [1, 50].
"""

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution(object):
  def splitListToParts(self, root, k):
    """
    :type root: ListNode
    :type k: int
    :rtype: List[ListNode]
    """
    if k == 1: return [root]

    # step 1: find num of nodes
    cnt = 0
    node = root
    while node is not None:
      node = node.next
      cnt += 1

    avr, rem = cnt / k, cnt % k
    cnt_ = [avr] * k
    for i in range(rem):
      cnt_[i] += 1

    # step 2: split
    # aux = ListNode(0)
    # aux.next = root
    # node = aux
    newnode = root
    ret = []
    for item in cnt_:
      # append head
      ret.append(newnode)
      # move to the end
      for i in range(item-1):
        newnode = newnode.next
      tmp = newnode
      if newnode is not None:
        newnode = newnode.next
      if tmp is not None:
        tmp.next = None
    return ret


if __name__ == "__main__":
  n1 = ListNode(1)
  n2 = ListNode(2)
  n3 = ListNode(3)
  n4 = ListNode(4)
  n5 = ListNode(5)

  n1.next = n2
  n2.next = n3
  n3.next = n4
  n4.next = n5

  a = Solution()
  res = a.splitListToParts(n1, 7)
  for node in res:
    if node is not None:
      print node.val
    else:
      print 'None'
