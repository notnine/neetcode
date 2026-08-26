from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anas = defaultdict(list) # key is sorted string, val is list of original strs

        for s in strs:
            anas[''.join(sorted(s))].append(s)
        
        return [value for key, value in anas.items()]