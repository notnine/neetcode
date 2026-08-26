class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = ""
        for d in digits:
            n += str(d)

        n_int = int(n)
        n_int += 1
        n_str = str(n_int)
        return [d for d in n_str]        
        