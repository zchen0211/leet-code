'''
401. Binary Watch (Easy)

A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.

For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
'''

class Solution(object):
  def Help_hour(self, num):
    result = []
    for i in range(13):
      # turn i to binary, check 1
      tmp = []
      tmp_i = i
      for j in range(4):
        tmp.append(tmp_i%2)
        tmp_i = tmp_i // 2
      tmp = tmp[::-1]
      if sum(tmp) == num:
        result.append(str(i))
    return result

  def Help_min(self, num):
    result = []
    for i in range(60):
      # turn i to binary, check 1
      tmp = []
      tmp_i = i
      for j in range(6):
        tmp.append(tmp_i%2)
        tmp_i = tmp_i // 2
      tmp = tmp[::-1]
      if sum(tmp) == num:
        result.append(str(i))
    return result

  def readBinaryWatch(self, num):
    if num == 0:
      return ['0:00']
    elif num>=10:
      return []
    
    result = []
    for i in range(min(4,num+1)): # i on in hours
      j = num - i
      if j < 0 or j > 6:
        continue
      result_h = self.Help_hour(i)
      result_m = self.Help_min(j)
      result_comb = [a+':'+b for a in result_h for b in result_m]
      result += result_comb
    return result
      

if __name__ == '__main__':
  a = Solution()
  print a.readBinaryWatch(1)
