class Solution {
public:
    int maxArea(vector<int>& height) {
        int n = height.size();
        int i = 0, j = n-1;
        int result = 0;
        
        while (j > i) {
            int tmp = min(height[i], height[j]) * (j - i);
            result = max(result, tmp);
            if (height[i] < height[j])
                ++i;
            else
                --j;
        }
        return result;
    }
};
