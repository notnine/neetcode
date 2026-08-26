class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {} # contains top 2 most freq. elements
        atleast = len(nums) // 3

        for n in nums:
            if n not in hashmap:
                hashmap[n] = 1
            else:
                hashmap[n] += 1
            
            if len(hashmap) == 3:
                keys = list(hashmap.keys())
                for k in keys:
                    hashmap[k] -= 1
                    if hashmap[k] == 0:
                        del hashmap[k]
            
        keys = list(hashmap.keys())
        for k in keys:
            if nums.count(k) <= atleast:
                del hashmap[k]
        
        return list(hashmap.keys())
