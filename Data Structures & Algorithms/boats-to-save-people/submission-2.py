class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # sort people in ascending order (n log n) time

        # 2 pointers, 1 @ start, 1 @ end. 
        # 1. try build boat with people at the 2 ptrs, if weight exceeds, just carry the person at the end.
        # 2. once a person is carried, move pointer. keep track of num of boats

        people.sort()
        l, r = 0, len(people) - 1
        res = 0 # num of boats so far

        while l <= r:
            if l == r:
                return res + 1
            
            curr = people[l] + people[r]
            if curr > limit:
                res += 1
                r -= 1
            else: # can carry both
                res += 1
                r -= 1
                l += 1

        return res
