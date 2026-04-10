"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        def get_start_time(interval) -> int:
            return interval.start
        
        def get_end_time(interval) -> int:
            return interval.end

        # find the max num of conflicting intervals at any 1 time
        res = 0
        min_heap = [] # sorted via end time (earliest to latest), tuples of (end time, start time)

        # sort by start time
        intervals.sort(key=get_start_time)

        # iterate thru intervals, at each interval, maintain a collection of currently occuring meetings w/ min heap
        for interval in intervals:
            print(min_heap)
            # pop the meetings that have ended
            while min_heap and min_heap[0][0] <= interval.start:
                heapq.heappop(min_heap)
            
            heapq.heappush(min_heap, (interval.end, interval.start))
            res = max(res, len(min_heap))
        
        return res

