class PrefixTree:
    class TrieNode: 
        def __init__(self): 
            self.childrenChars = {}
            self.char = None
        
    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:
        curNode = self.root
        for c in word: 
            if c not in curNode.childrenChars:
                newNode = self.TrieNode()
                newNode.char = c
                curNode.childrenChars[newNode.char] = newNode

            curNode = curNode.childrenChars[c]

        curNode.childrenChars["END"] = None

    def search(self, word: str) -> bool:
        curNode = self.root
        for c in word: 
            if c not in curNode.childrenChars:
                return False

            curNode = curNode.childrenChars[c] 

        return "END" in curNode.childrenChars

    def startsWith(self, prefix: str) -> bool:
        curNode = self.root
        for c in prefix: 
            if c not in curNode.childrenChars:
                return False
            curNode = curNode.childrenChars[c] 

        return True
        