'''
406. Queue Reconstruction by Height (Medium)

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''

class Solution(object):
  def reconstructQueue(self, people):
    """
    :type people: List[List[int]]
    :rtype: List[List[int]]
    """
    people.sort(key= lambda x: (x[1],x[0]))
    result = []
    print 'sorting...', people

    for item in people:
      h, n = item
      # check consistency
      front = 0
      for item2 in result:
        h2, n2 = item2
        if h2 >= h: 
          front += 1
      print 'current', item, front
      if front <= n:
        result.append([h, n])
      else:
        j = len(result) -1
        while(front>n):
          h2, n2 = result[j]
          if h2 >= h:
            front -= 1
          j -= 1
          print result[j], front
        result.insert(j+1, [h,n])
      print result
    return result


if __name__ == '__main__':
  a = Solution()
  print a.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
