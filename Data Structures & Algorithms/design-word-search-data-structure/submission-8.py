class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(i: int, node: Node):
            curr = node
            j = i

            for c in word[i:]:
                if c != '.':
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
                    j += 1
                else:
                    for child_node in curr.children.values():
                        if dfs(j+1, child_node):
                            return True
                    return False
            return True if curr.end else False

        return dfs(0, self.root)
        
