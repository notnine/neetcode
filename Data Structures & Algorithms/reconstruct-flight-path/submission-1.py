from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # instead of backtracking, just dont backtrack, just append airport to res when we know it's right
        # only add the airport once we've used all the outgoing neighbors from that airport
        # eulierian path: a path that consumes every edge, where nodes can repeat

        neighbors = defaultdict(list)
        tickets.sort(reverse=True)
        for src, dst in tickets:
            neighbors[src].append(dst)
        n = len(tickets) + 1
        res = []

        def dfs(src) -> bool:
            while neighbors[src]:
                nei = neighbors[src].pop() # traverese to next smallest nei
                dfs(nei)
            res.append(src) # no src is a dead end

        dfs("JFK")
        res.reverse()
        return res
        
    def findItineraryApproach0(self, tickets: List[List[str]]) -> List[str]:
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