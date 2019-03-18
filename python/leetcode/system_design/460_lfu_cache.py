"""
460. LFU Cache (Hard)

Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""

import collections


class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.table = {}  # original k: (v, freq)
        self.step = 0  # curr_step
        self.freq_2_key = {}  # frequency to [key]

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.table:
            # inc freq
            v, freq = self.table[key]
            self.table[key] = (v, freq + 1)
            self.freq_2_key[freq].remove(key)
            if len(self.freq_2_key[freq]) == 0:
                del self.freq_2_key[freq]
            if freq + 1 not in self.freq_2_key:
                self.freq_2_key[freq + 1] = [key]
            else:
                self.freq_2_key[freq + 1].append(key)
            return v
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.table:
            # reset
            v, freq = self.table[key]
            self.table[key] = (value, freq + 1)

            # change frequency
            self.freq_2_key[freq].remove(key)
            if len(self.freq_2_key[freq]) == 0:
                del self.freq_2_key[freq]
            if freq + 1 in self.freq_2_key:
                self.freq_2_key[freq + 1].append(key)
            else:
                self.freq_2_key[freq + 1] = [key]
        else:
            if self.capacity > 0:
                if len(self.table.keys()) == self.capacity:
                    # remove LF
                    min_freq = min(self.freq_2_key.keys())
                    k = self.freq_2_key[min_freq][0]
                    self.freq_2_key[min_freq].remove(k)
                    if len(self.freq_2_key[min_freq]) == 0:
                        del self.freq_2_key[min_freq]
                    del self.table[k]
                # add new
                self.table[key] = (value, 1)
                if 1 in self.freq_2_key:
                    self.freq_2_key[1].append(key)
                else:
                    self.freq_2_key[1] = [key]


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
