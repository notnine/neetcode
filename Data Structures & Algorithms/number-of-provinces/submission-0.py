class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) # path compression
        return self.parent[x]
    
    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)

        if self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = rootB
        elif self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA
        else:
            self.parent[rootB] = rootA
            self.rank[rootA] += 1 # because we added rootB to rootA, and their ranks were equal

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsu = DSU(n)

        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    dsu.union(i, j)
        
        # return number of unique roots
        roots = set()
        for i in range(n):
            roots.add(dsu.find(i))
        return len(roots)

