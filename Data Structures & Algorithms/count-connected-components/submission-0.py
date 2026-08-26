class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = set()
        res = 0

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def visit(node: int) -> None:
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    visit(nei)


        for node in range(n):
            if node not in visited:
                res += 1
                visit(node)

        return res

        