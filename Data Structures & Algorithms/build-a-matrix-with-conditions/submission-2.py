from collections import defaultdict

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # 2 ordering problems (rows, cols), where things must come before things.
        # topological sort (post order dfs) on both rows and cols
        # then get the row position and col position for each number
        # if cycle detected, then impossible & return empty matrix

        # 0. build adj graphs for row and col
        row_graph, col_graph = defaultdict(list), defaultdict(list)

        # we need all numbers 1 to k to be nodes
        for i in range(1, k+1):
            row_graph[i]
            col_graph[i]
        
        for a, b in rowConditions:
            row_graph[a].append(b)
        for a, b in colConditions:
            col_graph[a].append(b)
        
        # 1. build post order for both rows and cols using dfs
        row_postorder, col_postorder = [], []
        visiting, visited = set(), set()

        def dfs_row(node: int) -> bool:
            if node in visiting:
                return True
            if node in visited:
                return False

            visiting.add(node)
            for nei in row_graph[node]:
                if dfs_row(nei):
                    return True
            visiting.remove(node)
            visited.add(node)
            row_postorder.append(node)
            return False
        
        def dfs_col(node: int) -> bool:
            if node in visiting:
                return True
            if node in visited:
                return False

            visiting.add(node)
            for nei in col_graph[node]:
                if dfs_col(nei):
                    return True
            visiting.remove(node)
            visited.add(node)
            col_postorder.append(node)
            return False

        for i in range(1, k+1):
            if i not in visited:
                if dfs_row(i):
                    return []

        visiting, visited = set(), set()
        for i in range(1, k+1):
            if i not in visited:
                if dfs_col(i):
                    return []
        
        # 2. build hashmap mapping number to its index for both rows and cols
        num_to_row_index = {}
        # reverse our post order lists
        row_inorder, col_inorder = row_postorder[::-1], col_postorder[::-1]
        for i, num in enumerate(row_inorder):
            num_to_row_index[num] = i
        num_to_col_index = {}
        for i, num in enumerate(col_inorder):
            num_to_col_index[num] = i
        
        # 3. build matrix
        res = [[0 for _ in range(k)] for _ in range(k)]
        print(num_to_row_index)
        print(num_to_col_index)
        for num in range(1, k+1):
            r, c = num_to_row_index[num], num_to_col_index[num]
            res[r][c] = num
        
        return res

