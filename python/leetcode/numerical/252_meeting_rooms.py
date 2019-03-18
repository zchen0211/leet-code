"""
252. Meeting Rooms (Easy)

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return false.
"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if len(intervals) == 0:
            return True

        intervals.sort(key=lambda item: (item.start, item.end))

        n = len(intervals)
        for i in range(n - 1):
            int1 = intervals[i]
            int2 = intervals[i + 1]
            if int1.end > int2.start:
                return False
        return True
