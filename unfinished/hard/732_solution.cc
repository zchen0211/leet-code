/*
The logic is: let's walk though the start and end time points one by one in sorting order. If the point is start, increase one. If the point is end, decrease one. The sum is always greater or equal than 0, and it is the overlap number between the previous time to the next time.

This method can be used to solve My Calendar I and II as well.
*/

class MyCalendarThree {
public:
    MyCalendarThree() {
        
    }
    
    int book(int start, int end) {
        m[start]++;
        m[end]--;
        int res = 0;
        int cur = 0;
        for (auto & event: m)
        {
            cur += event.second;
            if (cur > res)
            {
                res = cur;
            }
        }
        return res;
    }
private:
    map<int, int> m;
};

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree obj = new MyCalendarThree();
 * int param_1 = obj.book(start,end);
 */
