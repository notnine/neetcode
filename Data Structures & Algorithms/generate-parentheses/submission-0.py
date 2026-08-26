class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []

        def backtrack(open_n: int, closed_n: int) -> None:
            if open_n == closed_n == n:
                res.append(''.join(curr))
                return
            
            if open_n < n:
                curr.append('(')
                backtrack(open_n + 1, closed_n)
                curr.pop()
            
            if closed_n < open_n:
                curr.append(')')
                backtrack(open_n, closed_n + 1)
                curr.pop()

        backtrack(0,0)
        return res    
        
