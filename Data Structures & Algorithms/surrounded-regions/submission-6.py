class Solution:
    def solve(self, board: List[List[str]]) -> None:      
        visited = set()
        free = set()
        neighbors = [(1,0), (0,1), (-1, 0), (0, -1)]
        def dfs(i,j): 
            for x,y in neighbors:
                nx, ny = i + x, j + y
                if 0<=nx<len(board) and 0<ny<len(board[0]) and (nx,ny) not in visited and board[nx][ny] == "O":
                    free.add((nx,ny))
                    visited.add((nx,ny))
                    dfs(nx,ny)

        for i in range(len(board)):
            for j in range(len(board[0])): 
                if board[i][j] == "O" and (i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0])-1):
                    free.add((i,j))
                    dfs(i,j)

        for i in range(len(board)):
            for j in range(len(board[0])): 
                if (i,j) not in free:
                    board[i][j] = "X"
