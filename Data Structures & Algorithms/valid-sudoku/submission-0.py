class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        #check rows
        for i in range(n): 
            row = set()
            for j in range(n):
                if board[i][j] in row and board[i][j] != ".":
                    return False
                row.add(board[i][j])

        #check cols
        for j in range(n): 
            col = set()
            for i in range(n):
                if board[i][j] in col and board[i][j] != ".":
                    return False
                col.add(board[i][j])
        
        #check box
        for startRow in range(0,9,3):
            for startCol in range(0,9,3): 
                sb = set()
                for j in range(3): 
                    for i in range(3):
                        boardVal = board[i+startRow][j+startCol]
                        if boardVal in sb and boardVal != ".":
                            return False
                        sb.add(boardVal)
        return True