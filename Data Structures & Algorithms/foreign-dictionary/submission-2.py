from collections import defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        # we can turn this problem into a graph, topological sort problem.
        # we can solve by doing post-order traversal via dfs

        letter_to_bigger = defaultdict(set) # set has no guaranteed order, but we can still iterate thru
        # initialize all chars as nodes
        for word in words:
            for c in word:
                letter_to_bigger[c] # init empty set

        # 0. build adj graph, mapping letter to bigger letters
        for i in range(len(words) - 1):
            curr_word = words[i]
            next_word = words[i+1]

            # if next_word is a prefix of curr_word, then invalid graph
            if len(next_word) < len(curr_word) and next_word == curr_word[:len(next_word)]:
                return ''
            
            # get first differing char, add that to our adj graph
            min_len = min(len(next_word), len(curr_word))
            j = 0
            while j < min_len and curr_word[j] == next_word[j]:
                j += 1
            if j < min_len: # only add to graph if j in bounds
                letter_to_bigger[curr_word[j]].add(next_word[j])

        # 1. post-order dfs to find topological sort
        res = [] # stores letters in traversed in post order
        visitted = set() # processed letters
        visitting = set() # visitting letters

        # return True if cycle detected
        def dfs(letter) -> bool:
            if letter in visitted:
                return False # letter has been processed

            visitting.add(letter)

            for nei in letter_to_bigger[letter]:
                if nei in visitting:
                    return True # cycle
                if dfs(nei):
                    return True

            visitting.remove(letter)
            visitted.add(letter)
            res.append(letter)
            return False

        for letter in letter_to_bigger:
            if dfs(letter):
                return ""
        
        return ''.join(res[::-1])
