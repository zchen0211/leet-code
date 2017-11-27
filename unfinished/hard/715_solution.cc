/*
The solution using vector of intervals (pair<int, int>) is very straightforward. The runtime is O(n) for addRange and deleteRange, and O(logn) for queryRange, where n is total number of intervals.

Another option is to use map (ordered map). And the runtime is still O(logn) for queryRange, but O(klogn) for addRange and deleteRange, where k is number of overlapping ranges.

For a single operation, it is hard to tell whether vector or map is better, because k is unknown. However, the k overlapping ranges will be erased after either add or remove ranges. Let's assume m is the total operations of add or delete ranges. Then total number of possible ranges is O(m) because add or delete may increase ranges by 1. So both n and k is O(m).

In summary, the run time for query is the same. However, the total run time for add and delete using vector is O(m^2), and that using map is O(mlogm). So amortized cost for delete and add is O(m) for vector, and O(logm) for map.
*/

// Vector

class RangeModule {
public:
   void addRange(int left, int right) {
        int n = invals.size();
        vector<pair<int, int>> tmp;
        for (int i = 0; i <= n; i++) {
            if (i == n || invals[i].first > right) {
                tmp.push_back({left, right});
                while (i < n) tmp.push_back(invals[i++]);
            }
            else if (invals[i].second < left) 
                tmp.push_back(invals[i]);
            else {
                left = min(left, invals[i].first);
                right = max(right, invals[i].second);
            }
        }
        swap(invals, tmp);
    }
    
    bool queryRange(int left, int right) {
        int n = invals.size(), l = 0, r = n-1;
        while (l <= r) {
            int m = l+(r-l)/2;
            if (invals[m].first >= right)
                r = m-1;
            else if (invals[m].second <= left)
                l = m+1;
            else 
                return invals[m].first <= left && invals[m].second >= right;
        }
        return false;
    }
    
    void removeRange(int left, int right) {
        int n = invals.size();
        vector<pair<int, int>> tmp;
        for (int i = 0; i < n; i++) {
            if (invals[i].second <= left || invals[i].first >= right)
                tmp.push_back(invals[i]);
            else {
                if (invals[i].first < left)  tmp.push_back({invals[i].first, left});
                if (invals[i].second > right) tmp.push_back({right, invals[i].second});
            }
        }
        swap(invals, tmp);
    }
private:
    vector<pair<int, int>> invals;
};

// Using map

class RangeModule {
public:
    void addRange(int left, int right) {
        auto l = invals.upper_bound(left), r = invals.upper_bound(right); 
        if (l != invals.begin()) {
            l--;
            if (l->second < left) l++;
        }
        if (l != r) {
            left = min(left, l->first);
            right = max(right, (--r)->second);
            invals.erase(l,++r);
        }
        invals[left] = right;
    }
    
    bool queryRange(int left, int right) {
        auto it = invals.upper_bound(left);
        if (it == invals.begin() || (--it)->second < right) return false;
        return true;
    }
    
    void removeRange(int left, int right) {
        auto l = invals.upper_bound(left), r = invals.upper_bound(right); 
        if (l != invals.begin()) {
            l--;
            if (l->second < left) l++;
        }
        if (l == r) return;
        int l1 = min(left, l->first), r1 = max(right, (--r)->second);
        invals.erase(l, ++r);
        if (l1 < left) invals[l1] = left;
        if (r1 > right) invals[right] = r1;
    }
private:
    map<int, int> invals;
};
