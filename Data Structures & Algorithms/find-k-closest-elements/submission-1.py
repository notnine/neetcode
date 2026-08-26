class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        # Edge cases
        if x <= arr[0]:
            return arr[:k]
        elif x >= arr[-1]:
            return arr[-k:]

        # Find the crossover point
        i = 0
        while i < len(arr) - 1 and not (arr[i] <= x and arr[i + 1] >= x):
            i += 1

        # Initialize two pointers
        a, b = i, i + 1
        res = []

        # Expand window from the center outwards
        while len(res) < k:
            if a < 0:
                res.append(arr[b])
                b += 1
            elif b >= len(arr):
                res.insert(0, arr[a])
                a -= 1
            else:
                if abs(arr[a] - x) <= abs(arr[b] - x):
                    res.insert(0, arr[a])
                    a -= 1
                else:
                    res.append(arr[b])
                    b += 1

        return res
