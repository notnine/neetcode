"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        def get_end_time(interval) -> int:
            return interval.end

        # sort by end time
        intervals.sort(key=get_end_time)

        # if next interval starts before curr interval ends, return false
        for i in range(0, len(intervals) - 1):
            curr_interval = intervals[i]
            next_interval = intervals[i+1]
            if curr_interval.end > next_interval.start:
                return False
        
        return True
