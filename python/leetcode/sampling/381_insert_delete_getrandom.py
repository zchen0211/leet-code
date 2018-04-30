'''
381. Insert Delete GetRandom O(1) - Duplicates allowed (Hard)

Design a data structure that supports all following operations in average O(1) time.

Note: Duplicate elements are allowed.
insert(val): Inserts an item val to the collection.
remove(val): Removes an item val from the collection if present.
getRandom: Returns a random element from current collection of elements. The probability of each element being returned is linearly related to the number of same value the collection contains.

Example:

// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();

// Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);

// Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1);

// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);

// getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();

// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);

// getRandom should return 1 and 2 both equally likely.
collection.getRandom();
'''
import random

class RandomizedCollection(object):
  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.nums = [] 
    self.num_2_id = {}     
    self.cnt = 0

  def insert(self, val):
    """
    Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
    :type val: int
    :rtype: bool
    """
    self.nums.append(val)
    self.cnt += 1
    if val in self.num_2_id:
      self.num_2_id[val].add(self.cnt-1)
      return False
    else:
      self.num_2_id[val] = set([self.cnt-1])
      return True

  def remove(self, val):
    """
    Removes a value from the collection. Returns true if the collection contained the specified element.
    :type val: int
    :rtype: bool
    """
    if val in self.num_2_id:
      last_val = self.nums[-1]
      # swap value and index
      val_id = self.num_2_id[val].pop()
      last_id = self.cnt -1
      self.nums[val_id], self.nums[last_id] = self.nums[last_id], self.nums[val_id]
      self.num_2_id[last_val].add(val_id)
      self.num_2_id[last_val].remove(last_id)
      self.nums = self.nums[:-1]
      self.cnt -= 1
      if len(self.num_2_id[val])==0:
        del self.num_2_id[val]
      return True
    else:
      return False

  def getRandom(self):
    """
    Get a random element from the collection.
    :rtype: int
    """
    tmp = random.randint(0, self.cnt-1)
    return self.nums[tmp]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

if __name__ == '__main__':
  obj = RandomizedCollection()
  print obj.insert(1)
  print obj.insert(1)
  print obj.insert(1)
  print obj.insert(2)
  print obj.num_2_id
  print obj.remove(1)
  print obj.num_2_id, obj.nums
  print obj.remove(2)
  print obj.num_2_id, obj.nums

