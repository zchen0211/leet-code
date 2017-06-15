'''
451. Sort Characters By Frequency (Medium)

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''

class Solution(object):
  def frequencySort(self, s):
    """
    :type s: str
    :rtype: str
    """
    c_stat = {}
    for i in range(len(s)):
      if s[i] in c_stat: c_stat[s[i]] += 1
      else: c_stat[s[i]] = 1

    c_stat = [(c, c_stat[c]) for c in c_stat]
    c_stat.sort(key= lambda x: x[1], reverse=True)
    result = ''
    for item in c_stat:
      c, n = item
      result += c * n
    return result


if __name__ == '__main__':
  a = Solution()
  print a.frequencySort('tree')
