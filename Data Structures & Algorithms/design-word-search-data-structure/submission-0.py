class WordDictionary:   
    class TrieNode: 
        def __init__(self): 
            self.childrenChars = {}
            self.end = False



    def __init__(self):
        self.root = self.TrieNode()

    def addWord(self, word: str) -> None:
        curNode = self.root
        
        for c in word: 
            if c not in curNode.childrenChars: 
                newNode = self.TrieNode()
                curNode.childrenChars[c] = newNode
            curNode = curNode.childrenChars[c]
            
        curNode.end = True
                

    def search(self, word: str) -> bool:
        
        def DFS(j, root):
            curNode = root

            for i in range(j,len(word)): 
                c = word[i]
                if c == '.': 
                    for child in curNode.childrenChars.values(): 
                        if DFS(i + 1, child): 
                            return True
                    
                    return False

                else:
                    if c not in curNode.childrenChars: 
                        return False

                    curNode = curNode.childrenChars[c]

            return curNode.end

        return DFS(0, self.root)

