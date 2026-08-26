class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        stone1 = heapq.heappop(stones) if stones else None
        stone2 = heapq.heappop(stones) if stones else None

        if not stone2:
            return -stone1

        while stone1 and stone2:
            if stone1 != stone2:
                result = min(stone1, stone2) - max(stone1, stone2)
                heapq.heappush(stones, result)
            
            stone1 = heapq.heappop(stones) if stones else None
            if not stones:
                return -stone1 if stone1 else 0
            else:
                stone2 = heapq.heappop(stones)
        
        return -stone1 if stone1 else 0
