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
