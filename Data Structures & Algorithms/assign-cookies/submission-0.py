class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        res = 0

        for child in g:
            # while this cookie cannot satisfy this child, go to the next cookie
            while i < len(s) and s[i] < child:
                i += 1
            # if this cookie can satisfy, increment res by 1
            if i < len(s) and s[i] >= child:
                res += 1
        
        return res