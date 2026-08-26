class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        digitToLetters = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res = []
        n = len(digits)

        def backtrack(curr: str, i: int) -> None:
            if i == n:
                res.append(curr)
                return
            
            digit = digits[i]
            for letter in digitToLetters[digit]:
                backtrack(curr + letter, i + 1)
            
        backtrack("",0)
        return res