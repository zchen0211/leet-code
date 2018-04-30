'''
275. H-Index II (Medium)

Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?

'''

class Solution(object):
  def hIndex(self, citations):
    n = len(citations)
    if n==0 or citations[n-1]==0:
      return 0
    # binary search
    st = 0
    end = n-1
    while(st<end):
      mid = (st+end)/2
      if n-mid == citations[mid]:
        return n-mid
      elif n-mid > citations[mid]:
        st = mid+1
      else:
        end = mid-1
      print st, mid, end
    if citations[st]>=n-st:
      return n-st
    else:
      return n-st-1

if __name__ == '__main__':
  a = Solution()
  print a.hIndex([0,0,1])
