class UnionFind:
    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    # return i's root
    def find(self, i: int) -> int:
        res = i
        while self.par[res] != res:
            self.par[res] = self.par[self.par[res]] # path compression: set parent to grandparent
            res = self.par[res]
        return res

    # return 0 if a & b are already in the same connected component, 1 otherwise
    def union(self, a: int, b: int) -> int:
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return 0
        
        # merge node with smaller rank into node with larger
        if self.rank[pa] > self.rank[pb]:
            self.par[pb] = pa
        elif self.rank[pa] < self.rank[pb]:
            self.par[pa] = pb
        else:
            self.par[pa] = pb
            self.rank[pb] += 1
        return 1
        
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        res = n
        for a, b in edges:
            res -= uf.union(a, b)
        return res

        