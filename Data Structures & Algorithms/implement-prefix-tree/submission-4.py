class Node: 
    def __init__(self):
        self.chars = {}

class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c in node.chars:
                node = node.chars[c]
            else:
                node.chars[c] = Node()
                node = node.chars[c]
        
        node.chars["end"] = True
        

        

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c in node.chars:
                node = node.chars[c]
            else:
                return False
        
        if "end" in node.chars: 
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c in node.chars:
                node = node.chars[c]
            else:
                return False
        return True