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
