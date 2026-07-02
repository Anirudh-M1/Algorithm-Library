class Node: 
    def __init__(self, c):
        self.val = c
        self.chars = {}

class PrefixTree:
    def __init__(self):
        self.root = Node(None)

    def insert(self, word: str) -> None:
        #print("in insert")
        node = self.root
        for c in word:
            #print(f"inserting {c}")
            if c in node.chars:
                node = node.chars[c]
            else:
                node.chars[c] = Node(c)
                node = node.chars[c]
        
        node.chars["end"] = True
        
        #print("insert done")

        

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            #print(f"current char is {c}")
            #print(f"children are {node.chars}")
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