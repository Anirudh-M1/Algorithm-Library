class TrieNode:
    def __init__(self): 
        self.children = {}
        self.isEnd = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
    
        for word in words:
            node = root 
        
            for c in word: 
                if c not in node.children: 
                    node.children[c] = TrieNode()
                
                node = node.children[c]
            
            node.isEnd = True

        wordList = set(words)
        visited = set()
        ans = set()
        neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def dfs(i,j,node, word):
            # print("->")
            # print(f"Current Char idx: {i,j} char = {board[i][j]}")
            # print(f"word so far: {word}")
            # print(f"possible paths {node.children}")

            if ((i, j)) in visited: 
                return 
            visited.add((i, j))
            
            if node.isEnd:
                ans.add(word)
                # print("added to the array")

           
            if not node.children:
                visited.remove((i,j))
                return

            for (nx, ny) in neighbors:
                if 0 <= i + nx <len(board) and 0 <= j + ny < len(board[0]) and (i+nx,j+ny):
                    # print(f"child is {board[i+ nx][j+ ny]}")
                    if board[i+nx][j + ny] in node.children:
                        dfs(i + nx, j + ny, node.children[board[i+nx][j + ny]], word+board[i+nx][j + ny])
                        
            visited.remove((i,j))

        for a in range(len(board)):
            for b in range(len(board[0])):
                if board[a][b] in root.children: 
                    # print(f"STARTING WITH LETTER {board[a][b]}")
                    dfs(a, b, root.children[board[a][b]], board[a][b])


        return list(ans)



