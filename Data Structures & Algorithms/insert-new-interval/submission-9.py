from collections import deque
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals = deque(intervals)
        res = []
        currInterval = intervals.popleft() if intervals else None

        # while newInterval does not conflict with currInterval, append to res
        while currInterval and currInterval[1] < newInterval[0]:
            res.append(currInterval)
            currInterval = intervals.popleft() if intervals else None
        
        # case 1: currInterval is None
        if currInterval is None:
            res.append(newInterval)
            return res
        
        # case 2: not conflict, but newInterval should be inserted first
        if currInterval[0] > newInterval[1]:
            res.append(newInterval)
            res.append(currInterval)
            if intervals:
                res.extend(intervals)
            return res
        
        # case 3: conflict, keep merging conflicting intervals
        while currInterval and (newInterval[1] >= currInterval[0]):
            newInterval[0] = min(currInterval[0], newInterval[0])
            newInterval[1] = max(currInterval[1], newInterval[1])
            currInterval = intervals.popleft() if intervals else None
        
        # case 2: no longer conflict
        res.append(newInterval)
        if currInterval:
            res.append(currInterval)
        if intervals:
            res.extend(intervals)
        return res