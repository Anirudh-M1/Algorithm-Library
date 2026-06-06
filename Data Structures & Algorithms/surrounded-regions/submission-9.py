class Solution:
    def solve(self, board: List[List[str]]) -> None:      
        visited = set()
        free = set()
        neighbors = [(1,0), (0,1), (-1, 0), (0, -1)]
        def dfs(i,j): 
            for x,y in neighbors:
                nx, ny = i + x, j + y
                if 0<=nx<len(board) and 0<ny<len(board[0]) and (nx,ny) not in visited and board[nx][ny] == "O":
                    board[nx][ny] = "#"
                    dfs(nx,ny)

        for i in range(len(board)):
            for j in range(len(board[0])): 
                if board[i][j] == "O" and (i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0])-1):
                    board[i][j] = "#"
                    dfs(i,j)

        for i in range(len(board)):
            for j in range(len(board[0])): 
                if board[i][j] == "#":
                    board[i][j] = "O"
                else: 
                    board[i][j] = "X"
