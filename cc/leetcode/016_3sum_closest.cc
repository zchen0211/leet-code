#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
		int i = 0;
		int j, k;
		vector<vector<int>> result;
		int n = nums.size();
        int result = nums[0] + nums[1] + nums[2];

		while (i < n - 2) {
			if (i > 0 and nums[i] == nums[i-1]) {
				++i;
				continue;
			}
			j = i + 1;
			k = n - 1;
			while (j < k) {
				if (j > i+1 and nums[j] == nums[j-1]) {
					++j;
					continue;
				}
				if (k != n-1 and nums[k] == nums[k+1]) {
					--k;
					continue;
				}
				int tmp = nums[i] + nums[j] + nums[k];
                if (abs(target-tmp) < abs(target-result))
					result = tmp;

				if (tmp > target)
					--k;
				else if (tmp < target)
					++j;
				else
					return target;
			}
			++i;
		}

		return result;
    }
};
