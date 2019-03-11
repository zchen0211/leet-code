"""
277. Find the Celebrity (Medium)

Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n), your function should minimize the number of calls to knows.

Note: There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.
"""

"""
brute force: O(n^2)

Good solution: O(n)
condition:
in-degree: n -1 
out-degree: 0

step 1:
celebrity candidate k start from 0:
for i = 1 .. n - 1
  if i knows k: 
  else: i becomes candidate
step 2: verify k

    int findCelebrity(int n) {
        int k = 0;
        for(int i = 1; i < n; i++)
            k = knows(i, k)?k:i;
        for(int i = 0; i < n; i++)
            if(i != k && (knows(k, i)||!knows(i, k)))
                return -1;
        return k;
    }
"""

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

know_set = set()
know_set.add((0,1))
know_set.add((0,2))
know_set.add((1,2))

def knows(a, b):
  return (a, b) in know_set

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1: return n - 1
        
        # candidate list
        cand = set(range(n))
        
        # step 1: 0 knows everyone?
        for i in range(1, n):
            tmp = knows(0, i)
            if tmp:
                if 0 in cand:
                    cand.remove(0)
            else:
                cand.remove(i)
                
        # step 2: go through
        for i in range(1, n):
            remove_list = []
            for j in cand:
                if i == j:
                    continue
                tmp = knows(i, j)
                if tmp:
                    remove_list.append(i)
                else:
                    remove_list.append(j)
            for j in remove_list:
                if j in cand: cand.remove(j)
            if len(cand) == 0: return -1
        
        # step 3: verify cand does not know anyone
        cand = list(cand)
        cand = cand[0]
        for i in range(n):
            if i == cand: continue
            if knows(cand, i):
                return -1
        return cand

print knows(0, 1)
print knows(0, 2)
print knows(1, 2)
a = Solution()
print a.findCelebrity(3)
