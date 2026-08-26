class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = [] # stores tuples ("dist", coords)

        for point in points:
            heapq.heappush(max_heap, (-(point[0]**2 + point[1]**2),point))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        return [point for dist, point in max_heap]