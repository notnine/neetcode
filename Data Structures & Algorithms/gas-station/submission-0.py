class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        total, res = 0, 0
        n = len(cost)

        for i in range(n):
            total = total + gas[i] - cost[i]

            if total < 0:
                total = 0
                res = i + 1

        return res