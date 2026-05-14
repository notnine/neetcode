class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        distinct, not_distinct = set(), set()

        for s in arr:
            if s not in distinct and s not in not_distinct:
                distinct.add(s)
            
            elif s in distinct:
                distinct.remove(s)
                not_distinct.add(s)
            
        i = 0
        for s in arr:
            if s in distinct:
                i += 1
            if i == k:
                return s
        
        return ''