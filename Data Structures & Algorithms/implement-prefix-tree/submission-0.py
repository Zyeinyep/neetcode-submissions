class Tree:
    def __init__(self):
        self.children = {}
        self.leaf = False
class PrefixTree:

    def __init__(self):
        self.root = Tree()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Tree()
            curr = curr.children[c]
            
        curr.leaf = True



    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.leaf

        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
        
        