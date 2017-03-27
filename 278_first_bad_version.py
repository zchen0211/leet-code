# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
  def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    begin = 1
    end = n
    while(begin<end):
      mid = (begin+end)/2
      if isBadVersion(mid):
        end = mid-1
      else:
        begin = mid+1
    if isBadVersion(begin):
      return begin
    else:
      return begin+1
