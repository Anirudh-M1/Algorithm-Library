class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        w = len(board[0])
        print(w)
        h = len(board)
        visited = set()
        wIdx = 0
        self.ans = False
    
        def dfs(i , j, wIdx):    
            if i < 0 or i >= h or j < 0 or j >= w: 
                return
            
            if (i,j) in visited:
                return

            if word[:wIdx] + board[i][j] == word: 
                print("set ans to true")
                self.ans = True
                return
            visited.add((i,j))

            if board[i][j] == word[wIdx]: 
                dfs(i+1, j, wIdx+1)
                dfs(i-1, j, wIdx+1)
                dfs(i, j+1, wIdx+1)
                dfs(i, j-1, wIdx+1)
        
            visited.remove((i,j))

        for i in range(h): 
            for j in range(w):
                dfs(i,j, 0)

        return self.ans
            