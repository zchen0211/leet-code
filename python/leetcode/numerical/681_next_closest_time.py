"""
681. Next Closest Time (Medium)

Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
"""

class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        # Notice time should be valid
        hh, mm = time.split(':')
        h1, h2 = int(hh[0]), int(hh[1])
        m1, m2 = int(mm[0]), int(mm[1])
        tmp_s = set([h1, h2, m1, m2])

        best = None
        b_diff = None
        for h1 in tmp_s:
          for h2 in tmp_s:
            for m1 in tmp_s:
              for m2 in tmp_s:
                hh = h1 * 10 + h2
                mm = m1 * 10 + m2
                if hh < 24 and mm < 60:
                  time2 = str(hh) + ':' + str(mm)
                  diff_ = self.diff(time, time2)
                  if b_diff is None or diff_ < b_diff:
                    print diff_, time2
                    b_diff = diff_
                    best = time2
        return best

    def diff(self, time1, time2):
       hh1, mm1 = time1.split(':')
       hh2, mm2 = time2.split(':')
       hh1, mm1 = int(hh1), int(mm1)
       hh2, mm2 = int(hh2), int(mm2)
       if hh1 < hh2 or (hh1 == hh2 and mm1 < mm2):
         diff = (hh2-hh1)*60 + mm2 - mm1
       else:
         diff = hh2 * 60 + mm2
         diff += (24-hh1) * 60 - mm1
       return diff


if __name__ == "__main__":
    a = Solution()
    print a.nextClosestTime("19:34")
    print a.nextClosestTime("23:59")
