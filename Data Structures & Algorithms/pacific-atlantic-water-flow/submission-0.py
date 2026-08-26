from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        n, m = len(heights), len(heights[0]) # n is num rows, m is cols
        
        # run bfs, find all pos that can reach atlantic. Last row/last col
        atla_visitted = set()
        curr_lvl = deque([])        
        for i in range(m):
            curr_lvl.append((n-1,i))
            atla_visitted.add((n-1,i))
        for i in range(n):
            curr_lvl.append((i,m-1))
            atla_visitted.add((i,m-1))
        
        while curr_lvl:
            next_lvl = []
            while curr_lvl:
                curr_i, curr_j = curr_lvl.popleft()
                for d_i, d_j in directions:
                    new_i, new_j = curr_i + d_i, curr_j + d_j
                    if 0 <= new_i < n and 0 <= new_j < m and (new_i, new_j) not in atla_visitted and heights[new_i][new_j] >= heights[curr_i][curr_j]:
                        # new pos can reach atlantic
                        atla_visitted.add((new_i,new_j))
                        next_lvl.append((new_i,new_j))
            curr_lvl = deque(next_lvl)

        print("reach atlantic: " + str(sorted(list(atla_visitted))))
        
        # now atla_visitted is a set that contains all pos that can reach atlantic. Do the same for pacific

        pac_visitted = set()
        curr_lvl = deque([])
        for i in range(m):
            curr_lvl.append((0,i))
            pac_visitted.add((0,i))
        for i in range(n):
            curr_lvl.append((i,0))
            pac_visitted.add((i,0))
        
        while curr_lvl:
            next_lvl = []
            while curr_lvl:
                curr_i, curr_j = curr_lvl.popleft()
                for d_i, d_j in directions:
                    new_i, new_j = curr_i + d_i, curr_j + d_j
                    if 0 <= new_i < n and 0 <= new_j < m and (new_i, new_j) not in pac_visitted and heights[new_i][new_j] >= heights[curr_i][curr_j]:
                        pac_visitted.add((new_i,new_j))
                        next_lvl.append((new_i,new_j))
            curr_lvl = deque(next_lvl)
        
        print("reach pacific: " + str(pac_visitted))

        both = pac_visitted & atla_visitted
        return list(both)

          