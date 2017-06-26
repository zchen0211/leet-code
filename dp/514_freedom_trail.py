"""
514. Freedom Trail (Hard)

In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom Trail Ring", and use the dial to spell a specific keyword in order to open the door.

Given a string ring, which represents the code engraved on the outer ring and another string key, which represents the keyword needs to be spelled. You need to find the minimum number of steps in order to spell all the characters in the keyword.

Initially, the first character of the ring is aligned at 12:00 direction. You need to spell all the characters in the string key one by one by rotating the ring clockwise or anticlockwise to make each character of the string key aligned at 12:00 direction and then by pressing the center button. 
At the stage of rotating the ring to spell the key character key[i]:
You can rotate the ring clockwise or anticlockwise one place, which counts as 1 step. The final purpose of the rotation is to align one of the string ring's characters at the 12:00 direction, where this character must equal to the character key[i].
If the character key[i] has been aligned at the 12:00 direction, you need to press the center button to spell, which also counts as 1 step. After the pressing, you could begin to spell the next character in the key (next stage), otherwise, you've finished all the spelling.

Example:

Input: ring = "godding", key = "gd"
Output: 4
Explanation:
 For the first key character 'g', since it is already in place, we just need 1 step to spell this character. 
 For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it become "ddinggo".
 Also, we need 1 more step for spelling.
 So the final output is 4.
Note:
Length of both ring and key will be in range 1 to 100.
There are only lowercase letters in both strings and might be some duplcate characters in both strings.
It's guaranteed that string key could always be spelled by rotating the string ring.
"""

class Solution(object):
  def findRotateSteps(self, ring, key):
    """
    :type ring: str
    :type key: str
    :rtype: int
    """
    c_pos = self.helper(ring)
    last_pos = [0]
    last_cnt = [0]
    n = len(ring)
    for c in key:
      new_pos = c_pos[c]
      new_cnt = []
      for tmp_new in new_pos: # new position
        min_ = n+last_cnt[0]
        for i in range(len(last_pos)):
          tmp_last = last_pos[i]
          step1 = (tmp_new-tmp_last) % n
          step2 = n - step1
          min_ = min(min_, last_cnt[i]+min(step1, step2))
        new_cnt.append(min_)
      print 'char: ', c, new_pos, new_cnt
      last_pos, last_cnt = new_pos, new_cnt
    return min(new_cnt) + len(key)

  def helper(self, ring):
    # give a ring return position as a dictionary
    c_pos = {}
    for i in range(ord('a'), ord('z')+1):
      c_pos[chr(i)] = []
    for i in range(len(ring)):
      c_pos[ring[i]].append(i)
    return c_pos


if __name__ == '__main__':
  a = Solution()
  print a.findRotateSteps('godding', 'gdooi')
  # print a.helper('godding')
