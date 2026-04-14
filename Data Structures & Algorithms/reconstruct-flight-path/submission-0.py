from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # sort tickets
        # run dfs + backtracking, naturally the first path is alphabetically the smallest

        neighbors = defaultdict(list)
        tickets.sort()
        for src, dst in tickets:
            neighbors[src].append(dst)
        n = len(tickets) + 1
        res = ["JFK"]

        def dfs(src) -> bool: # return True if we have traversed n airports
            if len(res) == n:
                return True
            
            src_neighbors = neighbors[src]
            for i, nei in enumerate(src_neighbors):
                # try traversing into nei, if that doesnt work backtrack
                res.append(nei)
                # pop from the real neighbors
                neighbors[src].pop(i)
                found_sol = dfs(nei)
                if found_sol:
                    return True
                src_neighbors.insert(i, nei) # reinsert into real neighbors
                res.pop()

        dfs("JFK")
        return res