class Solution(object):
  def findRadius(self, houses, heaters):
    """
    :type houses: List[int]
    :type heaters: List[int]
    :rtype: int
    """
    # heaters
    heaters.sort()

    # check houses one by one by bst search
    max_radius = 0
    for house in houses:
      # check nearest heater
      st_id = 0
      end_id = len(heaters) - 1
      mid_id = (st_id + end_id)/2
      while(st_id<mid_id):
        if house > heaters[mid_id]:
          st_id = mid_id
        elif house < heaters[mid_id]:
          end_id = mid_id
        else:
          st_id = mid_id
          break
        mid_id = (st_id + end_id) /2
      print st_id, ',', end_id
      min_dist = min( abs(house-heaters[st_id]), abs(house-heaters[end_id]))
      print min_dist
      max_radius = max(max_radius, min_dist)
    return max_radius


if __name__ == '__main__':
  a = Solution()
  print a.findRadius([1,2,3,4],[1,4])
