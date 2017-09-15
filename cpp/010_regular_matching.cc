#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        return helper(s, p, 0, 0);
    }

    bool helper(string s, string p, int i, int j) {
    	int ls = s.length();
    	int lp = p.length();
    	// boundary condition
    	if (i == ls) {
    	    while (j < lp - 1 and p[j+1] == '*')
            	j += 2;
            return j == lp;
        } else if (j == lp)
            return i == ls;

        cout << s[i] << " " << p[j] << endl;

        if (j < lp - 1 and p[j+1] == '*') {
            char c = p[j];
            // new j position, remove same c*c* ...
            j += 2;
            while (j < lp - 1 and p[j] == c and p[j+1] == '*')
               j += 2;
            // new i position: [i..i_end]
            int i_end = i;
            if (c == '.') i_end = ls;
            else {
                while (i_end < ls and s[i_end] == c)
                    ++i_end;
            }
            cout << "positions: " << i_end << i << " " << j << endl;
            for (int ii = i_end; ii >= i; --ii) {
                cout << "here" << endl;
                cout << ii << j << endl;
                if (helper(s, p, ii, j))
                    return true;
            }
            return false;
        } else if (s[i] == p[j] or p[j] == '.')
            return helper(s, p, i+1, j+1);
        else
            return false;
    }
};

int main() {
    Solution a;
    cout << a.isMatch(string("a"), string(".*..a*"));
    return 0;
}
