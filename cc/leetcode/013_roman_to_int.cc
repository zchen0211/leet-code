#include <string>
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        vector<vector<string>> rec;
		rec.push_back(vector<string>({"M", "-", "-"}));
		rec.push_back(vector<string>({"C", "D", "M"}));
		rec.push_back(vector<string>({"X", "L", "C"}));
		rec.push_back(vector<string>({"I", "V", "X"}));

        int result = 0;
        int i = 0;
		int s_i = 0;
        while (s_i < s.length()) {
			int tmp = 0;
			if (startswith(s, s_i, rec[i][0] + rec[i][1])) {
				tmp = 4;
				s_i += 2;
			} else if (startswith(s, s_i, rec[i][0] + rec[i][2])) {
				tmp = 9;
				s_i += 2;
			} else {
				if (startswith(s, s_i, rec[i][1])) {
					tmp = 5;
					s_i++;
				}
                while (s_i < s.length() and s[s_i] == rec[i][0][0]) {
					++s_i;
					++tmp;
				}
			}
			cout << s_i << " " << tmp << endl;
			switch (i) {
				case 0: result += tmp * 1000;
						break;
				case 1: result += tmp * 100;
						break;
				case 2: result += tmp * 10;
						break;
				case 3: result += tmp;
						break;
			}
			cout << "result: " << result << endl;
			++i;
			cout << i << s.length() << endl;
        }
		return result;
    }

    bool startswith(string s, int i, string prefix) {
        cout << s << " " << i << " " << prefix << endl;
        if (s.length() < i + prefix.length())
			return false;
		int n = prefix.length();
		for (int ii = 0; ii < n; ++ii) {
			// cout << s[i+ii] << " " << prefix[ii] << endl;
        	if (s[i+ii] != prefix[ii])
				return false;
		}
		return true;
    }
};

int main() {
	string s("DCXXI");
	Solution a;
	cout << a.romanToInt(s);
	return 0;
}

