from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = Counter(tasks).values()
        maxHeap = [-freq for freq in freqs]
        heapq.heapify(maxHeap)
        cooldown = deque([])

        t = 0

        while maxHeap or cooldown:
            f = heapq.heappop(maxHeap) if maxHeap else None
            if f and f+1 != 0:
                cooldown.append((f+1, t+n))
            if cooldown and cooldown[0][1] == t:
                heapq.heappush(maxHeap, cooldown.popleft()[0])
            t += 1
        
        return t