class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        charToLast = {} # maps a char to its last index in s

        for i, c in enumerate(s):
            charToLast[c] = i

        # make as many parts. as possible. keep track of the curr "latest last" index within the curr part. 
        curr = 0 # curr part's last index
        part_len = 0
        for i, c in enumerate(s):
            part_len += 1
            curr = max(curr, charToLast[c])
            if i == curr: # make new part
                res.append(part_len)
                part_len =  0
                curr = 0
        
        return res