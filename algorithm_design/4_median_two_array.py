'''
4. Median of Two Sorted Arrays (Hard)

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''

class Solution(object):
  def findMedian(self, nums1, nums2):
    m = len(nums1)
    n = len(nums2)
    st = 0
    end = m
    if m == 0:
      if n%2 == 0:
        return float(nums2[n/2]+nums2[n/2-1])/2.
      else:
        return nums2[n/2]
    elif n == 0:
      if m%2 == 0:
        return float(nums1[m/2]+nums1[m/2-1])/2.
      else:
        return nums1[m/2]
    
    while(st != end):
      i = (st+end)/2
      j = (m+n+1)/2 - i
      print 'arr1: ', nums1[:i], 'arr2: ', nums2[:j]
      if j>n or (i<m and j>0 and nums2[j-1]>nums1[i]):
        # increase i if n2[0..j] too long or n2[j-1]>n1[i]
        print 'case 1'
        st = i+1
      elif j<0 or (i>0 and (j<n and nums1[i-1]>nums2[j])):
        # decrease i if needed
        print 'case 2'
        end = i-1
      else:
        print 'case 3'
        st, end = i, i
        break
      print 'start ', st, 'end ', end, 'i ', i
    i = st
    j = (m+n+1)/2-i
    print 'i', i, 'j', j
    if (m+n)%2 == 1:
      if i>0 and j>0:
        max_left = max(nums1[i-1], nums2[j-1])
      elif i<m:
        max_left = nums1[i-1]
      else:
        max_left = nums2[j-1]
      return float(max_left)
    else:
      if i>0 and j>0:
        max_left = max(nums1[i-1], nums2[j-1])
      elif i==0 and j>0:
        max_left = nums2[j-1]
      else:
        max_left = nums1[i-1]

      if i<m and j<n:
        min_right = min(nums1[i], nums2[j])
      elif i<m:
        min_right = nums1[i]
      else:
        min_right = nums2[j]
      return float(max_left+min_right)/2.


if __name__ == '__main__':
  a = Solution()
  print a.findMedian([1,3], [2])
  # print a.findMedian([1,2], [3,4])
  # print a.findMedian([100], [101])
  # print a.findMedian([2,3,4], [1])
  # print a.findMedian([1,2,3,5], [4])
  # print a.findMedian([1], [2,3,4,5,6])
  # print a.findMedian([1,2,3,4,5,7,8,9,10], [6])
