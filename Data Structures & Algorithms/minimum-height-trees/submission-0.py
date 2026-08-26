#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#

# @lc code=start
from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n < 3:
            return [i for i in range(n)]
        
        # build adj list adj & degree list
        degree = [0 for _ in range(n)]
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        leaves = []
        for i in range(n):
            if degree[i] == 1:
                leaves.append(i)
        
        remaining = n

        # peel of layer by layer of leaves, similar to bfs
        while remaining > 2:
            next_leaves = []
            for leaf in leaves:
                # leaf_neighbour = adj[leaf][0] # leaf only has 1 neighbour
                for nei in adj[leaf]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        next_leaves.append(nei)
                remaining -= 1
                
            leaves = next_leaves
        
        return leaves
        

# @lc code=end

