"""
393. UTF-8 Validation (Medium)

A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

For 1-byte character, the first bit is a 0, followed by its unicode code.
For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.
This is how the UTF-8 encoding would work:

   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Given an array of integers representing the data, return whether it is a valid utf-8 encoding.

Note:
The input is an array of integers. Only the least significant 8 bits of each integer is used to store the data. This means each integer represents only 1 byte of data.

Example 1:

data = [197, 130, 1], which represents the octet sequence: 11000101 10000010 00000001.

Return true.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
Example 2:

data = [235, 140, 4], which represented the octet sequence: 11101011 10001100 00000100.

Return false.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.
"""

class Solution(object):
  def validUtf8(self, data):
    """
    :type data: List[int]
    :rtype: bool
    """
    n = len(data)
    i = 0
    cnt = 0
    while(i<n):
      n1 = data[i]
      # print n1, n1>>5
      if cnt == 0:
        if n1>>5 == 0b110:
          # print 'here'
          cnt = 1
        elif n1>>4 == 0b1110:
          cnt = 2
        elif n1>>3 == 0b11110:
          cnt = 3
        elif n1>>7 == 0b1: return False
      else:
        if n1>>6 != 0b10: return False
        cnt -= 1
      i += 1 
    return cnt == 0

  def binarize(self, num):
    result = []
    for i in range(8):
      result.append(num%2)
      num /= 2
    result = result[::-1]
    return result


if __name__ == '__main__':
  a = Solution()
  print a.validUtf8([197,130,1])
  print a.validUtf8([235,140,4])
