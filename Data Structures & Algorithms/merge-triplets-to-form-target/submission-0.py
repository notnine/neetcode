class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valids = [] # triplets where no element is larger than target

        for a, b, c in triplets:
            if not (a > target[0] or b > target[1] or c > target[2]):
                valids.append([a,b,c])

        target_a, target_b, target_c = target
        found_a, found_b, found_c = False, False, False
        for a, b, c in valids:
            if a == target_a:
                found_a = True
            if b == target_b:
                found_b = True
            if c == target_c:
                found_c = True
            
        return found_a and found_b and found_c


