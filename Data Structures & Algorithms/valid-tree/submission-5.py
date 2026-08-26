class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree: all nodes are connected & no cycles
        nodeToNeis = defaultdict(list)
        for n1, n2 in edges:
            if n1 == n2:
                return False
            nodeToNeis[n1].append(n2)
            nodeToNeis[n2].append(n1)
        visitted = set()

        def dfs(node: int, prev: int) -> bool:

            for nei in nodeToNeis[node]:
                if nei != prev and nei in visitted:
                    return False
                if nei != prev and nei not in visitted:
                    visitted.add(nei)
                    if not dfs(nei, node):
                        return False
            
            return True
        
        visitted.add(0)
        return dfs(0,-1) and len(visitted) == n
