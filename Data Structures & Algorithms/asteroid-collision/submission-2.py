class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        curr = []
        asteroids = deque(asteroids)
        curr.append(asteroids.popleft())

        while asteroids:
            opp = asteroids.popleft()
            # curr loses = curr blown up but opp not blown up
            # while curr is not empty and top of curr loses to opp 
            while curr and curr[-1] > 0 and opp < 0 and abs(curr[-1]) < abs(opp):
                curr.pop()
            if curr and curr[-1] > 0 and opp < 0 and -curr[-1] == opp:
                curr.pop()
            elif curr and curr[-1] > 0 and opp < 0 and abs(-curr[-1]) > abs(opp):
                continue
            else:
                curr.append(opp)
        
        return curr
