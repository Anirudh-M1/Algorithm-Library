class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False
from functools import cache
class WordDictionary:

    def __init__(self):
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]

        node.isEnd = True 

    def search(self, word: str) -> bool:
        node = self.root

        @cache
        def dfs(i, node):
            if i >= len(word):
                return node.isEnd
            
            if word[i] == ".":
                for p in node.children.keys(): 
                    if dfs(i + 1, node.children[p]):
                        return True 
            elif word[i] in node.children: 
                return dfs(i+1, node.children[word[i]])
            else:
                return False
            
            return node.isEnd and i >= len(word)

        return dfs(0, self.root) 