from collections import deque

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        def get_end(interval: List[int]) -> int:
            return interval[1]
        
        intervals.sort(key=get_end)
        q = deque(intervals)
        curr = q.popleft() if q else None
        res = 0

        print(intervals)
        print()

        while curr and q:
            # if overlap increment res
            if curr[1] > q[0][0]:
                res += 1
                q.popleft()
            else:
                curr = q.popleft()
        
        return res