class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        start_big = [1]
        start_small = [1]
        n = len(arr)

        for i in range(1, n):
            num = arr[n - i - 1]

            if num > arr[n - i]:
                start_big_next = 1 + start_small[-1]
                start_small_next = 1
            elif num < arr[n - i]:
                start_small_next = 1 + start_big[-1]
                start_big_next = 1
            else:
                start_big_next = 1
                start_small_next = 1
            
            start_big.append(start_big_next)
            start_small.append(start_small_next)
        
        return max(max(start_big), max(start_small))