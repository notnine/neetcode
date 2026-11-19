class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        first = 0
        curr = 0

        for bit in derived:
            if bit == 0:
                continue
            else:
                curr = ~curr
        
        return first == curr