class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {} # our 2 most freq. elements
        atleast = len(nums) // 3

        for n in nums:
            print(hashmap)
            if n not in hashmap:
                hashmap[n] = 1
            else:
                hashmap[n] += 1
            
            if len(hashmap) == 3:
                keys = list(hashmap.keys())
                for key in keys:
                    hashmap[key] -= 1
                    if hashmap[key] == 0:
                        del hashmap[key]
                        
        keys = list(hashmap.keys())
        for key in keys:
            if nums.count(key) <= atleast:
                del hashmap[key]

        return list(hashmap.keys()) 