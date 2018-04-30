'''
423. Reconstruct Original Digits from English (Medium)

Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
Example 1:
Input: "owoztneoer"

Output: "012"
Example 2:
Input: "fviefuro"

Output: "45"
'''
import collections

class Solution(object):
  def originalDigits(self, s):
    """
    :type s: str
    :rtype: str
    """
    stat = dict(collections.Counter(s))
    record = [0] * 10
    print stat
    # check 0, 2, 6, 7, 8, 9 first
    record[0] = self.helper(stat, 'zero', 'z')
    record[2] = self.helper(stat, 'two', 'w')
    record[6] = self.helper(stat, 'six', 'x')
    record[7] = self.helper(stat, 'seven', 's')
    record[8] = self.helper(stat, 'eight', 'g')
    record[4] = self.helper(stat, 'four', 'u')
    record[5] = self.helper(stat, 'five', 'f')
    record[1] = self.helper(stat, 'one', 'o')
    record[3] = self.helper(stat, 'three', 't')
    record[9] = self.helper(stat, 'nine', 'i')
    
    result = ''
    for i in range(10):
      result += str(i)*record[i]
    return result

  def helper(self, stat, tmp_str, key, time=1):
    if key in stat:
      n = stat[key]/time
      for i in range(len(tmp_str)):
        stat[tmp_str[i]] -= n
        if stat[tmp_str[i]] == 0: del stat[tmp_str[i]]
    else:
      return 0
    return n

if __name__ == '__main__':
  a = Solution()
  print a.originalDigits("owoztneoer")
  print a.originalDigits("fviefuro")
