class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        l, r = 0, 0
        whites = 0
        blacks = 0
        res = float('inf')

        while r < len(blocks):
            if blocks[r] == 'W':
                whites += 1
            else:
                blacks += 1
            
            if whites + blacks == k:
                res = min(res, whites)
            
            # when do we shrink our window?
            while l < r and blocks[l] == 'W':
                l += 1
                whites -= 1
            
            r += 1
        
        return res
