'''
275. H-Index II (Medium)

Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?

'''

"""
n numbers sorted:

find index k, s.t.
  1. array[k] and n-k as close as possible;
  2. array[k] >= n-k
then h-index at least n-k

case 1: citations[mid] == len-mid, then it means there are citations[mid] papers that have at least citations[mid] citations.
case 2: citations[mid] > len-mid, then it means there are citations[mid] papers that have moret than citations[mid] citations, so we should continue searching in the left half
case 3: citations[mid] < len-mid, we should continue searching in the right side
After iteration, it is guaranteed that right+1 is the one we need to find (i.e. len-(right+1) papars have at least len-(righ+1) citations)

int hIndex(vector<int>& citations) {
    int left=0, len = citations.size(), right= len-1,  mid;
    while(left<=right)
    {
        mid=(left+right)>>1;
        if(citations[mid]== (len-mid)) return citations[mid];
        else if(citations[mid] > (len-mid)) right = mid - 1;
        else left = mid + 1;
    }
    return len - (right+1);
}
"""

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
