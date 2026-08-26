class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {} # stores result of wordBreak(s) where s is a string

        def gang_gang(s: str, wordDict: List[str]) -> bool:
            if not s:
                return True

            if s in memo:
                return memo[s]
            
            for word in wordDict:
                n = len(word)
                if s[:n] == word: # can try word
                    if s[n:] not in memo:
                        memo[s[n:]] = gang_gang(s[n:], wordDict)
                    if memo[s[n:]]:
                        return True
            memo[s] = False
            return False

        return gang_gang(s, wordDict)