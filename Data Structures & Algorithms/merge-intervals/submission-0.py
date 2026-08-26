from collections import deque

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        def get_start(interval: List[int]):
            return interval[0]

        res = []
        intervals.sort(key=get_start)
        intervals = deque(intervals)
        res.append(intervals.popleft())

        curr_interval = intervals.popleft() if intervals else None
        while curr_interval:
            # if curr_interval overlaps with last merged interval (top of res), merge
            if res and res[-1][1] >= curr_interval[0]:
                res[-1][1] = max(res[-1][1], curr_interval[1])
            # else append to res
            else: 
                res.append(curr_interval)
            curr_interval = intervals.popleft() if intervals else None
        
        return res