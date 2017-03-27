'''
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
'''

class Solution(object):
  def numberOfBoomerangs(self, points):
    cnt = 0
    for p in points:
      # go through and save in hash map
      cmap = {}
      for q in points:
        dis = (p[0]-q[0])**2 + (p[1]-q[1])**2
        if cmap.has_key(dis):
          cmap[dis] += 1
        else:
          cmap[dis] = 1
      # 
      for k,v in cmap.items():
        cnt += v * (v-1)
    
    return cnt


if __name__ == '__main__':
  a = Solution()
  print a.numberOfBoomerangs([[0,0],[1,0],[2,0]])
