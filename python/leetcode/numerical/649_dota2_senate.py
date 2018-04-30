"""
649. Dota2 Senate (Medium)

In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the senate wants to make a decision about a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

Ban one senator's right: 
A senator can make another senator lose all his rights in this and all the following rounds.
Announce the victory: 
If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and make the decision about the change in the game.
Given a string representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party respectively. Then if there are n senators, the size of the given string will be n.

The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party, you need to predict which party will finally announce the victory and make the change in the Dota2 game. The output should be Radiant or Dire.

Example 1:
Input: "RD"
Output: "Radiant"
Explanation: The first senator comes from Radiant and he can just ban the next senator's right in the round 1. 
And the second senator can't exercise any rights any more since his right has been banned. 
And in the round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.
Example 2:
Input: "RDD"
Output: "Dire"
Explanation: 
The first senator comes from Radiant and he can just ban the next senator's right in the round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And the third senator comes from Dire and he can ban the first senator's right in the round 1. 
And in the round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.
Note:
The length of the given string will in the range [1, 10,000].
"""

import collections

class Solution(object):
  def predict(self, senate):
    n = len(senate)
    flag = [True] * n

    cnt_map = dict(collections.Counter(senate))
    R_cnt = cnt_map.get('R', 0)
    D_cnt = cnt_map.get('D', 0)
    print R_cnt, D_cnt

    i = 0 # who is voting
    while R_cnt != 0 and D_cnt != 0:
      if not flag[i]:
        i = (i+1)%n
        continue
      j = (i+1)%n
      while senate[j]==senate[i] or flag[j]==False:
        j = (j+1)%n
      if senate[j] == 'R':
        R_cnt -= 1
      else:
        D_cnt -= 1
      flag[j] = False
      i = (i+1)%n
    print flag
    if D_cnt == 0:
      return "Radiant"
    else:
      return "Dire"
     
  def solve2(self, senate):
    n = len(senate)
    tmp = 0 # >0 for d votes, <0 for r votes
    k = 0
    while True: # senate != 'R'*n or senate != 'D'*n:
      # i = 0
      # if senate[i] == 'D': tmp += 1
      # else: tmp -= 1
      sub = ""
      for i in range(n):
        if senate[i] == 'D':
          if tmp >= 0:
            sub += senate[i]
          tmp += 1
        else: # senate[j] == 'R'
          if tmp <= 0:
            sub += senate[i]
          tmp -= 1
        print i, tmp, sub
      print 'finish! ', sub
      senate = sub
      n = len(senate)
      cnt = dict(collections.Counter(senate))
      if cnt.get('R', 0) == 0: break
      if cnt.get('D', 0) == 0: break
      # k += 1
      # print senate, n, senate == 'R'*n
      # if k== 2: break
    if cnt.get('R', 0) != 0: return "Radiant"
    else: return "Dire"

if __name__ == "__main__":
  a = Solution()
  print a.solve2("RDD")
