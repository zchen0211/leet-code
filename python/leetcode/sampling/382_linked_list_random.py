'''
382. Linked List Random Node (Medium)

Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

Example:

// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();
'''

import random

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.data = []
        tmp = head
        while(tmp):
          self.data.append(tmp.val)
          tmp = tmp.next

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        t = random.randint(0, len(self.data)-1)
        return self.data[t]


class solution2(object):
  # AC2: reservoir sampling
  # slower, but better space complexity
  def __init__(self, head):
    self.head = head

  def getRandom(self):
    cnt = 1
    tmp = self.head
    ret = tmp.val
    tmp = tmp.next
    while tmp is not None:
      cnt += 1
      v = random.randint(0, cnt-1)
      if v % cnt == 0: ret = tmp.val
      tmp = tmp.next
      # print v, cnt, ret
    return ret


if __name__ == '__main__':
  head = ListNode(0)
  n1 = ListNode(1)
  n2 = ListNode(2)
  n3 = ListNode(3)

  head.next = n1
  n1.next = n2
  n2.next = n3

  a = solution2(head)
  result = []
  for i in range(100):
    result.append(a.getRandom())
  print result
  print result.count(0)
  print result.count(1)
  print result.count(2)
  print result.count(3)
# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
