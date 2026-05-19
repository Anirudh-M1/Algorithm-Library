class TrieNode: 
    def __init__(self): 
        self.childrenNodes = {}
        self.isWord = False
    
    def addWord(self, word): 
        curNode = self
        for c in word:
            if c not in curNode.childrenNodes: 
                curNode.childrenNodes[c] = TrieNode()
            curNode = curNode.childrenNodes[c]

        curNode.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        
        for word in words:
            root.addWord(word)
        
        rows, cols = len(board), len(board[0])
        res, visit = set(), set()
            
        def DFS(r, c, node, word): 
            if r<0 or c<0 or r == rows or c == cols:
                return  

            if (r,c) in visit or board[r][c] not in node.childrenNodes:
                return
            
            visit.add((r,c))
            node = node.childrenNodes[board[r][c]]
            word += board[r][c]
            if node.isWord: 
                res.add(word)

            DFS(r-1, c, node, word)
            DFS(r+1, c, node, word)
            DFS(r, c-1, node, word)
            DFS(r, c+1, node, word)
            visit.remove((r,c))

        for r in range(rows): 
            for c in range(cols):
                DFS(r, c, root, "")

        return list(res)
        