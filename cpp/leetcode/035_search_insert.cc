#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int n = nums.size();
		int i = 0, j = n;
		while (i < j) {
			int mid = (i + j) / 2;
			if (nums[mid] > target)
				j = mid;
			else if (nums[mid] == target)
				return mid;
			else
				i = mid + 1;
		}
		return max(i, j);
    }
};
