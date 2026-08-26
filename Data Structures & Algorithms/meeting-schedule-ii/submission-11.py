"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import deque

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)

        start = [interval.start for interval in intervals]
        end = [interval.end for interval in intervals]
        start.sort()
        end.sort()

        s_i, e_i = 0, 0 # start index, end index
        res = 0
        curr = 0 # keep track of # conflicting meetings at a given time

        print(start)
        print(end)

        while s_i < n and e_i < n:
            # conflict if start before end
            if start[s_i] < end[e_i]:
                curr += 1
                res = max(res, curr)
                s_i += 1
            else:
                curr -= 1
                e_i += 1
            
        return res
