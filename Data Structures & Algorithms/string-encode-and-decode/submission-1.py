class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            n = str(len(s))
            res += n + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            n = int(s[i:j])
            j += 1
            curr = ""
            for idx in range(j,j+n):
                curr += s[idx]
            res.append(curr)
            i = j + n
        return res
