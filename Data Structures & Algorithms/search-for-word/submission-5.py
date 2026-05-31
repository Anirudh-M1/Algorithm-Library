class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.found = False

        def dfs(i,j,word):
            #out of bounds or used, skip         
            if len(word) == 0:
                self.found = True
                return

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or (i,j) in self.visited: 
                return
            
            if word[0] == board[i][j]: 
                self.visited.add((i,j))
                dfs(i + 1, j, word[1:])
                dfs(i, j + 1, word[1:])
                dfs(i - 1, j, word[1:])
                dfs(i, j - 1, word[1:])
                self.visited.remove((i,j))
        for i in range(len(board)): 
            for j in range(len(board[0])): 
                self.visited = set()
                dfs(i,j,word)
        return self.found