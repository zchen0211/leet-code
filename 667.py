class Solution(object):
  def cons(self, n, k):
    if k == 1: return range(1, n+1)
    # solve first k
    min_ = 1
    max_ = k+1
    result = []
    while min_ <= max_:
      result.append(min_)
      min_ += 1
      if max_ > min_:
        result.append(max_)
        max_ -= 1
    tail = range(k+2, n+1)
    result = result + tail

    '''

    l2 = l2[::-1]
    print l1, l2
    result = []
    for i in range(len(l2)):
      result.append(l1[i])
      result.append(l2[i])
    if len(l1)>len(l2): result.append(l1[-1])
    print result
    tail = range(k+2, n+1)
    result = result + tail
    '''
    return result


if __name__ == "__main__":
  a = Solution()
  # print a.cons(3,1) 
  res = a.cons(100,40)
  tmp_set = set()
  for i in range(len(res)-1):
    tmp_set.add( abs(res[i]-res[i+1]))
  print tmp_set, len(tmp_set)
