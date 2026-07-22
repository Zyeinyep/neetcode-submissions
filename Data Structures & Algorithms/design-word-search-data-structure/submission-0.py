class Tree:
    def __init__(self):
        self.children = {}
        self.leaf = False
class WordDictionary:

    def __init__(self):
        self.root = Tree()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Tree()
            curr = curr.children[c]
        curr.leaf = True
        
        

    def search(self, word: str) -> bool:
        curr = self.root
        def dfs(i, node):
            if i == len(word):
                return node.leaf
            c = word[i]
            if c != '.':
                    if c not in node.children:
                        return False
                    return dfs(i + 1, node.children[c])
            else:
                for child in node.children.values():
                    if dfs(i + 1, child):
                        return True
            return False
            
        return dfs(0, curr)
        
