class Solution {
    bool dfs(vector<int> &sidesLength,const vector<int> &matches, int k, int target, int index) {
        if (index == matches.size()) {
            for (int i = 0; i < k; ++i) {
                if (sidesLength[i] != target)
                    return false;
            }
            return true;
        }
        
        for (int i = 0; i < k; ++i) {
            if (sidesLength[i] + matches[index] > target)
                continue;
            else {
                sidesLength[i] += matches[index];
                if (dfs(sidesLength, matches, k, target, index + 1))
                    return true;
                sidesLength[i] -= matches[index];
            }
        }
        return false;
    }
public:
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        if (nums.empty()) return false;
        if (k == 1)
            return true;
        int total = 0;
        for (int i = 0; i < nums.size(); ++i)
            total += nums[i];
        if (total % k != 0)
            return false;
        int target = total / k;
        vector<int> sidesLength(k, 0);
        std::sort(nums.begin(), nums.end(), std::greater<int>());

        return dfs(sidesLength, nums, k, target, 0);
    }
};
