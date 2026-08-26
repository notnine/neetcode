class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(i: int) -> int:
            s = str(i)
            return sum((int(d) * int(d) for d in s))

        slow = n
        fast = get_next(n)

        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        
        return fast == 1