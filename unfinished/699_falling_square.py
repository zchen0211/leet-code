"""
699. Falling Squares (Hard)

On an infinite number line (x-axis), we drop given squares in the order they are given.

The i-th square dropped (positions[i] = (left, side_length)) is a square with the left-most point being positions[i][0] and sidelength positions[i][1].

The square is dropped with the bottom edge parallel to the number line, and from a higher height than all currently landed squares. We wait for each square to stick before dropping the next.

The squares are infinitely sticky on their bottom edge, and will remain fixed to any positive length surface they touch (either the number line or another square). Squares dropped adjacent to each other will not stick together prematurely.


Return a list ans of heights. Each height ans[i] represents the current highest height of any square we have dropped, after dropping squares represented by positions[0], positions[1], ..., positions[i].

Example 1:
Input: [[1, 2], [2, 3], [6, 1]]
Output: [2, 5, 5]
Explanation:

After the first drop of positions[0] = [1, 2]:
_aa
_aa
-------
The maximum height of any square is 2.


After the second drop of positions[1] = [2, 3]:
__aaa
__aaa
__aaa
_aa__
_aa__
--------------
The maximum height of any square is 5.  
The larger square stays on top of the smaller square despite where its center
of gravity is, because squares are infinitely sticky on their bottom edge.


After the third drop of positions[1] = [6, 1]:
__aaa
__aaa
__aaa
_aa
_aa___a
--------------
The maximum height of any square is still 5.

Thus, we return an answer of [2, 5, 5].


Example 2:
Input: [[100, 100], [200, 100]]
Output: [100, 100]
Explanation: Adjacent squares don't get stuck prematurely - only their bottom edge can stick to surfaces.
Note:

1 <= positions.length <= 1000.
1 <= positions[i][0] <= 10^8.
1 <= positions[i][1] <= 10^6.
"""

class Solution(object):
  def search(self, hori, target):
    # binary search
    i, j = 0, len(hori) - 1
    # find first idx, s.t. hori[idx] >= target
    while i < j:
      mid = (i + j) / 2
      if hori[mid] > target:
        j = mid
      elif hori[mid] == target:
        return mid
      else:
        i = mid + 1
    idx = min(i, j)
    return idx

  def fallingSquares(self, positions):
    """
    :type positions: List[List[int]]
    :rtype: List[int]
    """
    hori = [0]
    hei = [0]
    ret = []

    # init the skyline
    begin, len_ = positions[0]
    hori.append(begin)
    hori.append(begin+len_)
    hei.append(len_)
    hei.append(0)

    ret = [len_]
    print 'init', hori, hei
    for item in positions[1:]:
      begin, len_ = item
      end = begin + len_
      if end > hori[-1]:
        hori.append(end)
        hei.append(0)

      if begin >= hori[-1]:
        if begin == hori[-1]:
          hori.append(end)
          hei[-1] = len_
          hei.append(0)
        else:
          hori.append(begin)
          hori.append(end)
          hei.append(len_)
          hei.append(0) 
      elif end <= hori[1]:
        if end == hori[1]:
          hori.insert(1, begin)
          hei.insert(1, len_)
        else:
          hori.insert(1, begin)
          hei.insert(1, len_)
          hori.insert(2, end)
          hei.insert(2, 0)

      else:
        idx1 = self.search(hori, begin)
        print 'begin', begin, hori, idx1

        idx2 = self.search(hori, end)
        print 'end', end, hori, idx2

        # update hori and height
        if idx1 == idx2:
          if hori[idx1] > begin:
            tmp_hei = hei[idx1-1]
          else:
            tmp_hei = hei[idx1]
          hori.insert(idx1, begin)
          hei.insert(idx1, tmp_hei+len_) 
          hori.insert(idx1+1, end) 
          hei.insert(idx1+1, tmp_hei)
        else:
          if hori[idx1] > begin:
            tmp_max = max(hei[idx1-1:idx2])
          else:
            tmp_max = max(hei[idx1:idx2])
          hori.insert(idx2, end) 
          hei.insert(idx2, hei[idx2-1]) 
          print 'tmp_max', tmp_max
          final = tmp_max + len_
          for idx in range(idx1, idx2):
            hei[idx] = final
          hori[idx1] = idx1
        
      print hori, hei
      ret.append(max(hei))
    return ret


if __name__ == "__main__":
  a = Solution()
  # arr = [[100, 100], [200, 100]]
  # arr = [[1, 2], [2, 3], [6, 1]]
  # arr = [[1,5],[2,2],[7,5]] # ans: 5, 7, 7
  # arr = [[4,9],[8,8],[6,8],[8,2],[1,2]] # ans: [9, 17, 25, 27, 27]
  arr = [[5,10],[1,7],[1,2],[9,3],[1,6]]
  # arr = [[5,10],[1,7]]
  print a.fallingSquares(arr)
