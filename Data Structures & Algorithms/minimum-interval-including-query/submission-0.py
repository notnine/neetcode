import heapq
from collections import defaultdict

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        def get_interval_start(interval: List[int]) -> int:
            return interval[0]

        # sort intervals by start time, queries in incr. order.
        # maintain min heap (duration, start time, end time) of intervals
        # for each query:
        # push to min heap if this interval start <= q
        # keep popping head if head end < q
        # head is this q's ans
        # notice we might have "invalid" intervals in our min heap for this q, but doesn't matter till they reach head

        res = defaultdict(int) # maps queries to result
        intervals.sort(key=get_interval_start)
        sorted_queries = sorted(queries) # sorted deep copy
        i, n = 0, len(intervals) # ptr to intervals
        min_heap = []

        for q in sorted_queries:
            while i < n and get_interval_start(intervals[i]) <= q:
                heapq.heappush(min_heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][0], intervals[i][1]))
                i += 1
            while min_heap and min_heap[0][2] < q:
                heapq.heappop(min_heap)
            res[q] = min_heap[0][0] if min_heap else -1
        
        final_res = []
        for q in queries:
            final_res.append(res[q])
        
        return final_res
            