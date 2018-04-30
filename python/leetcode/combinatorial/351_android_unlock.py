"""
351. Android Unlock Patterns (Medium)

Given an Android 3x3 key lock screen and two integers m and n, where 1 <= m <= n <= 9, count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.

Rules for a valid pattern:
 1. Each pattern must connect at least m keys and at most n keys.
 2. All the keys must be distinct.
 3. If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
 4. The order of keys used matters.

Explanation:
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Invalid move: 4 - 1 - 3 - 6 
Line 1 - 3 passes through key 2 which had not been selected in the pattern.

Invalid move: 4 - 1 - 9 - 2
Line 1 - 9 passes through key 5 which had not been selected in the pattern.

Valid move: 2 - 4 - 1 - 3 - 6
Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern

Valid move: 6 - 5 - 4 - 1 - 9 - 2
Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.

Example:
Given m = 1, n = 1, return 9.

Credits:
Special thanks to @elmirap for adding this problem and creating all test cases.
"""

class Solution(object):
  def numberOfPatterns(self, m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    if m == 0: return 1
    if m > 9: return 0
    n = min(n, 9)

    curr = [[]]

    step = 1
    accu = 0
    if m == 0: accu += 1

    while step <= n:
      new = []
      for tmplist in curr:
        for i in range(1, 10):
          if len(tmplist) == 0:
            new_list = [item for item in tmplist]
            new_list.append(i)
            new.append(new_list)
          else:
            # check valid
            if i in tmplist: # already visited
              continue
            i1, j1 = (tmplist[-1]-1)/3, (tmplist[-1]-1)%3
            i2, j2 = (i-1)/3, (i-1)%3
            if (i1+i2)%2 == 0 and (j1+j2)%2 == 0:
              i3, j3 = (i1+i2)/2, (j1+j2)/2
              idx = i3 * 3 + j3 + 1
              if idx not in tmplist:
                continue
            new_list = [item for item in tmplist]
            new_list.append(i)
            new.append(new_list)
      if step >= m and step <= n:
        accu += len(new)
      step += 1
      print new
      new, curr = curr, new
    return accu
   

if __name__ == "__main__":
  a = Solution()
  print a.numberOfPatterns(1, 3)
