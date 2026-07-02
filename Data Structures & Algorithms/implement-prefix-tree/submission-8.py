class Node: 
    def __init__(self):
        self.chars = {}
        self.isEnd = False

class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.chars:
                node.chars[c] = Node()
            
            node = node.chars[c]
        
        node.isEnd = True
        
    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c in node.chars:
                node = node.chars[c]
            else:
                return False
        
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c in node.chars:
                node = node.chars[c]
            else:
                return False
        return True