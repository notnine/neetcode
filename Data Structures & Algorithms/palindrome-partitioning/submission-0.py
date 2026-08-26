class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(curr: List[str], curr_str: str, i: int) -> None:
            print("curr: " + str(curr))
            print("curr str: " + str(curr_str))
            print("i: " + str(i))
            print("res: " + str(res))
            print()
            
            if i == len(s):
                if curr_str == curr_str[::-1] and curr_str:
                    curr.append(curr_str)
                    res.append(curr.copy())
                    curr.pop()
                    return
                else:
                    return
            
            if curr_str == curr_str[::-1] and curr_str:
                curr.append(curr_str)
                backtrack(curr, s[i], i+1)
                curr.pop()
            backtrack(curr, curr_str + s[i], i + 1)
        
        backtrack([], "", 0)
        return res