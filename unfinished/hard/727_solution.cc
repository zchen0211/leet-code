/*
For substring S[0, i] and T[0, j], 
dp[i][j] is starting index k of the shortest postfix of S[0, i], such that T[0, j] is a subsequence of S[k, i]. 
Here T[0] = S[k], T[j] = S[i]. Otherwise, dp[i][j] = -1.

The goal is the substring with length of min(i-dp[i][n-1]) for all i < m,  where m is S.size() and n is T.size() 
Initial condition: dp[i][0] = i if S[i] = T[0], else -1
Equations: If S[i] = T[j], dp[i][j] = max(dp[k][j-1]) for all k < i; else dp[i][j] = -1;      
*/

// O(mn) space 82 ms

class Solution {
public:
    string minWindow(string S, string T) {
        int m = S.size(), n = T.size();
        vector<vector<int>> dp(n, vector<int>(m, -1));
        for (int i = 0; i < m; i++) 
            if (S[i] == T[0]) dp[0][i] = i;
        for (int j = 1; j < n; j++) {
            int k = -1;
            for (int i = 0; i < m; i++) {
                if (k != -1 && S[i] == T[j]) dp[j][i] = k;
                if (dp[j-1][i] != -1) k = dp[j-1][i];
            }
        }
        int st = -1, len = INT_MAX;
        for (int i = 0; i < m; i++) {
            if (dp[n-1][i] != -1 && i-dp[n-1][i]+1 < len) {
                st = dp[n-1][i];
                len = i-dp[n-1][i]+1;
            }    
        }
        return st == -1? "":S.substr(st, len);
    }
};

// O(m) space 53 ms

class Solution {
public:
    string minWindow(string S, string T) {
        int m = S.size(), n = T.size();
        vector<int> dp(m, -1);
        for (int i = 0; i < m; i++) 
            if (S[i] == T[0]) dp[i] = i;
        for (int j = 1; j < n; j++) {
            int k = -1;
            vector<int> tmp(m, -1);
            for (int i = 0; i < m; i++) {
                if (k != -1 && S[i] == T[j]) tmp[i] = k;
                if (dp[i] != -1) k = dp[i];
            }
            swap(dp, tmp);
        }
        int st = -1, len = INT_MAX;
        for (int i = 0; i < m; i++) {
            if (dp[i] != -1 && i-dp[i]+1 < len) {
                st = dp[i];
                len = i-dp[i]+1;
            }    
        }
        return st == -1? "":S.substr(st, len);
    }
};
