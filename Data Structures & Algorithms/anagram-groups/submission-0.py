class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaToStrings = defaultdict(list)

        for s in strs:
            curr = tuple(sorted(s))
            anaToStrings[curr].append(s)
        return list(anaToStrings.values())