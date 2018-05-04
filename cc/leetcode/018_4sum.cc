#include <iostream>
#include <vector>
#include <unordered_map>
#include <set>

using namespace std;

class Solution {
public:
    vector<vector<int> > fourSum(vector<int>& nums, int target) {
        int n = nums.size();
		vector<vector<int> > result;
		if (n < 4)
			return result;
		unordered_map<int, vector<vector<int> > > mapping;

		// step 0: build hash table
		for (int i = 0; i < n; ++i) {
			for (int j = i + 1; j < n; ++j) {
				int tmp = nums[i] + nums[j];
				if (mapping.find(tmp) == mapping.end())
					mapping[tmp] = vector<vector<int> >();
				mapping[tmp].push_back({i, j});
			}
		}

		set<string> visited;

		for (auto& item : mapping) {
			int comp = target - item.first;
			if (mapping.find(comp) != mapping.end()) {
				for (auto& comb1 : item.second) {
					for (auto& comb2 : mapping[comp]) {
						// check no duplicate in comb1 and comb2
						vector<int> comb({comb1[0], comb1[1], comb2[0], comb2[1]});
						sort(comb.begin(), comb.end());
						bool valid = true;
						
						for (int i = 0; i < 3; ++i) {
							if (comb[i] == comb[i+1])
								valid = false;
						}
						if (valid) {
							vector<int> tmp_;
							for (int i = 0; i < 4; ++i) {
								tmp_.push_back(nums[comb[i]]);
							}
							sort(tmp_.begin(), tmp_.end());
							// check no duplicate
							// add to visit
							bool found = duplicate(visited, tmp_);
							// push back to result
							if (!found)
								result.push_back(tmp_);
						}
					}
				}
			}
		}

		return result;
    }

	bool duplicate(set<string>& visited, vector<int>& tmp_) {
		string s;

		for (int i = 0; i < 4; ++i)
			s = s + to_string(tmp_[i]) + " ";
		bool found = visited.find(s) != visited.end();

		if (!found)
			visited.insert(s);
		return found;
	}
};

int main() {
	Solution a;
	vector<int> arr({1, 0, -1, 0, -2, 2});
	vector<vector<int> > result = a.fourSum(arr, 0);
	for (auto& sub : result) {
		for (int i = 0; i < 4; ++i)
	  		cout << sub[i] << " ";
		cout << endl;
	}
	return 0;
}
