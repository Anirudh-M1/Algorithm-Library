class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c):
            if (r, c) in visited or board[r][c] != "O":
                return
            visited.add((r, c))
            for nr, nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0 <= nr < rows and 0 <= nc < cols:
                    dfs(nr, nc)

        # Step 1: Mark all 'O's connected to the border
        for r in [0, rows-1]:
            for c in range(cols):
                dfs(r, c)
        for r in range(rows):
            for c in [0, cols-1]:
                dfs(r, c)

        # Step 2: Flip all unvisited 'O's to 'X'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in visited:
                    board[r][c] = 'X'
