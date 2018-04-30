#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        unordered_map<char, vector<char>> mapping;
		mapping['1'] = vector<char>();
		mapping['2'] = vector<char>({'a', 'b', 'c'});
		mapping['3'] = vector<char>({'d', 'e', 'f'});
		mapping['4'] = vector<char>({'g', 'h', 'i'});
		mapping['5'] = vector<char>({'j', 'k', 'l'});
		mapping['6'] = vector<char>({'m', 'n', 'o'});
		mapping['7'] = vector<char>({'p', 'q', 'r', 's'});
		mapping['8'] = vector<char>({'t', 'u', 'v'});
		mapping['9'] = vector<char>({'w', 'x', 'y', 'z'});
		mapping['*'] = vector<char>({'+'});
		mapping['0'] = vector<char>({' '});
		mapping['#'] = vector<char>();

		vector<string> result({""});
		vector<string> new_result;
		if (digits.find("1") != string::npos)
			return result;
		int n = digits.length();
		if (n == 0)
			return vector<string>();

		for (int i = 0; i < n; ++i) {
			char c = digits[i];
			new_result.clear();
			vector<char> c_list = mapping[c];
			for (auto& item : result) {
				for (auto& c_ : c_list) {
					new_result.push_back(item + c_);
				}
			}
			swap(result, new_result);
		}
		return result;
    }
};

int main() {
	Solution a;
	vector<string> result = a.letterCombinations("23");
	for (auto& item : result)
		cout << item << endl;
	return 0;
}
