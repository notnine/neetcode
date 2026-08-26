class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # build adj list; dictionary mapping vertex to list of neighbours
        vertexToNeis = defaultdict(list)
        for v1, v2 in edges:
            vertexToNeis[v1].append(v2)
            vertexToNeis[v2].append(v1)

        # dfs
        # remember the entry point of the cycle, keep track of the nodes in the cycle
        # once we reach the starting point (keep track) of the cycle we return
        # return true when unwinding cycle

        entry = -1
        visited = set() # individual nodes we visited
        cycle = set() # individual nodes within cycle

        # return true when unwinding cycle
        def dfs(node: int, par: int) -> bool:
            nonlocal entry

            if node in visited and entry == -1: # start of cycle
                entry = node
                cycle.add(node)
                return True
            
            visited.add(node)
            neis = vertexToNeis[node]
            for nei in neis:
                if nei == par:
                    continue
                if dfs(nei, node): # unwinding a cycle
                    if node == entry: # done with cycle. mark as done
                        entry = -69
                    if entry != -69 and node not in cycle:
                        cycle.add(node)
                    return True # because we are still unwinding a cycle
            return False
            
        print(cycle)

        dfs(1, -1)
        for v1, v2 in edges[::-1]:
            if v1 in cycle and v2 in cycle:
                return [v1,v2]

        