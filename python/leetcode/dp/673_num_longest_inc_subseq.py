"""
673. Number of Longest Increasing Subsequence (Medium)

Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int."""

"""
The idea is to use two arrays len[n] and cnt[n] to record the maximum length of Increasing Subsequence and the coresponding number of these sequence which ends with nums[i], respectively. That is:

len[i]: the length of the Longest Increasing Subsequence which ends with nums[i].
cnt[i]: the number of the Longest Increasing Subsequence which ends with nums[i].

Then, the result is the sum of each cnt[i] while its corresponding len[i] is the maximum length.

Java version:

public int findNumberOfLIS(int[] nums) {
        int n = nums.length, res = 0, max_len = 0;
        int[] len =  new int[n], cnt = new int[n];
        for(int i = 0; i<n; i++){
            len[i] = cnt[i] = 1;
            for(int j = 0; j <i ; j++){
                if(nums[i] > nums[j]){
                    if(len[i] == len[j] + 1)cnt[i] += cnt[j];
                    if(len[i] < len[j] + 1){
                        len[i] = len[j] + 1;
                        cnt[i] = cnt[j];
                    }
                }
            }
            if(max_len == len[i])res += cnt[i];
            if(max_len < len[i]){
                max_len = len[i];
                res = cnt[i];
            }
        }
        return res;
    }
C++ version: (use vector<pair<int, int>> dp to combine len[] and cnt[])

    int findNumberOfLIS(vector<int>& nums) {
        int n = nums.size(), res = 0, max_len = 0;
        vector<pair<int,int>> dp(n,{1,1});            //dp[i]: {length, number of LIS which ends with nums[i]}
        for(int i = 0; i<n; i++){
            for(int j = 0; j <i ; j++){
                if(nums[i] > nums[j]){
                    if(dp[i].first == dp[j].first + 1)dp[i].second += dp[j].second;
                    if(dp[i].first < dp[j].first + 1)dp[i] = {dp[j].first + 1, dp[j].second};
                }
            }
            if(max_len == dp[i].first)res += dp[i].second;
            if(max_len < dp[i].first){
                max_len = dp[i].first;
                res = dp[i].second;
            }
        }
        return res;
    }
"""

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0

        seq = [max(nums)+1] * n
        stat = []
        for i in range(n): stat.append({})

        seq[0] = nums[0]
        stat[0][nums[0]] = 1

        curr_len = 1
        for i in range(1, n):
          item = nums[i]
          # look up update stat
          id_ = self.lookup(seq, curr_len, item)
          # print item, seq, id_
          seq[id_] = item

          if id_ == 0: inc = 1
          else:
            inc = 0
            for k in stat[id_-1].keys():
                if k < item:
                    inc += stat[id_-1][k]

          if item in stat[id_]:
            stat[id_][item] += inc
          else:
            stat[id_][item] = inc
          # print 'after', item, seq, id_, stat
          if id_ == curr_len:
            curr_len += 1
        return sum(stat[curr_len-1].values())
    
    def lookup(self, seq, curr_len, item):
        # look up in seq[0:curr_len]
        # search id_ s.t. seq[id_] >=  item
        i = 0
        j = curr_len
        while i < j:
          mid = (i + j) / 2
          if seq[mid] == item: return mid
          elif seq[mid] < item:
            i = mid + 1
          else:
            j = mid
        return i
