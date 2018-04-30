"""
251. Flatten 2D Vector (Medium)

Implement an iterator to flatten a 2d vector.

For example,
Given 2d vector =

[
  [1,2],
  [3],
  [4,5,6]
]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].

Follow up:
As an added challenge, try to code it using only iterators in C++ or iterators in Java.
"""

class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.data = vec2d
        self.idx = None

    def next(self):
        """
        :rtype: int
        """
        i, j = self.idx
        return self.data[i][j]

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.data) == 0:
          return False
        if self.idx is None:
          self.idx = [0, 0]
        else:
          i, j = self.idx
          j += 1
          self.idx = [i, j]

        i, j = self.idx
        # get to the next index return True
        if j < len(self.data[i]):
          return True

        i, j = i+1, 0
        while i != len(self.data):
          if len(self.data[i]) > 0:
            self.idx = [i, j]
            return True
          else:
            i, j = i+1, 0
        return False


if __name__ == "__main__":
  vec = [[1,2], [3], [4,5,6]]
  i, v = Vector2D(vec), []
  while i.hasNext():
    v.append(i.next())
    print v
# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
