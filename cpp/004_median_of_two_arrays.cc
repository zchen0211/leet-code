#include <iostream>
#include <vector>

using std::vector;
using std::cout;
using std::endl;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();

        int st = 0, end = m;
        int i, j;

        if (m == 0) {
            if (n % 2 == 0)
                return float(nums2[n/2]+nums2[n/2-1])/2.;
            else
                return float(nums2[n/2]);
        } else if (n == 0) {
            if (m % 2 == 0)
                return float(nums1[m/2]+nums1[m/2-1])/2.;
            else
                return float(nums1[m/2]);
        }

        while (st != end) {
            i = (st + end) / 2;
            j = (m + n + 1) / 2 - i;

            // increase i if i has right and nums1[i+1] < nums2[j]
            if (j>n or (i<m and j>0 and nums2[j-1]>nums1[i])) {
                st = i + 1;}
            else if (j<0 or (i>0 and j<n and nums1[i-1]>nums2[j])) {
                end = i - 1;}
            else {
                st = i;
                end = i;
                break;
            }
            cout << i << " " << j << endl;
        }
        cout << "here 0";
        i = st;
        j = (m+n+1)/2-st;
        cout << i << " " << j << endl;
        cout << "here 0";
        int max_left;
        if (i>0 and j>0) {
            std::cout << "here 1";
            max_left = std::max(nums1[i-1], nums2[j-1]);}
        else if (i > 0) {
            std::cout << "here 2";
            max_left = nums1[i-1];}
        else {
            std::cout << "here 3";
            max_left = nums2[j-1];}
        std::cout << "here";
        if ((m+n)%2 == 1)
            return float(max_left);
        else {
            int min_right;
            if (i<m and j<n) {
                min_right = std::min(nums1[i], nums2[j]);
            } else if (i<m) {
                min_right = nums1[i];
            } else {
                min_right = nums2[j];
            }
            return float(max_left+min_right)/2.;
        }
    }
};

int main() {
    vector<int> nums1={2, 4};
    vector<int> nums2={5, 7};
    Solution a;
    float result = a.findMedianSortedArrays(nums1, nums2);
    std::cout << result << std::endl;
    return 0;
}
