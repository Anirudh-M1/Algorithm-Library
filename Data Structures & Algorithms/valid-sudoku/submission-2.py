from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(len(board)): 
            for c in range(len(board[0])): 
                val = board[r][c]
                if val == ".": 
                    continue
                if val in rows[r] or val in cols[c] or val in boxes[r//3+(c//3)*len(board)]: 
                    print(f"dup val is {val}")
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[r//3+(c//3)*len(board)].add(board[r][c])

        return True