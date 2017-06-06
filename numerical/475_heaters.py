'''
475. Heaters (Easy)

Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:
Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
As long as a house is in the heaters' warm radius range, it can be warmed.
All the heaters follow your radius standard and the warm radius will the same.
Example 1:
Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
Example 2:
Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.
'''

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
