#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
		int i = 0;
		int j, k;
		vector<vector<int>> result;
		int n = nums.size();

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
				int target = nums[i] + nums[j] + nums[k];
				if (target > 0)
					--k;
				else if (target < 0)
					++j;
				else {
					result.push_back(vector<int>({nums[i], nums[j], nums[k]}));
					++j;
					--k;
				}
			}
			++i;
		}

		return result;
    }
};
