class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set) # key = col index
        rows = collections.defaultdict(set) # key = row index
        boxs = collections.defaultdict(set) # key = (col//3, row//3)
        
        for c in range(9):
            for r in range(9):
                if board[r][c] == ".":
                    continue
                elif (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in boxs[(r//3, c//3)]):
                    return False
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                boxs[(r//3, c//3)].add(board[r][c])
        return True