'''
384. Shuffle an Array (Medium)

Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
'''
import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.original_data = nums
        self.data = [item for item in nums] 

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.data = [item for item in self.original_data]
        return self.data

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        random.shuffle(self.data)
        return self.data

class solution2(object):
  def __init__(self, nums):
    self.data = nums

  def reset(self):
    return self.data

  def shuffle(self):
    shuffled = self.data[:] # get a deep copy
    n = len(self.data)
    i = n-1
    while i>0:
      # for i in range(n):
      id_ = random.randint(0,i)
      shuffled[i], shuffled[id_] = shuffled[id_], shuffled[i]
      i -= 1
    return shuffled

if __name__ == '__main__':
  a = solution2(range(3))
  for i in range(20):
    print a.shuffle()

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
