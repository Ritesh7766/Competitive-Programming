class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        mp_row = collections.defaultdict(set)
        mp_col = collections.defaultdict(set)
        mp_grid = collections.defaultdict(set)
        
        for i in range(N):
            for j in range(N):
                if board[i][j] == '.': continue
                
                if board[i][j] in mp_row[i]: return False
                if board[i][j] in mp_col[j]: return False
                if board[i][j] in mp_grid[(i // 3, j // 3)]: return False
                
                mp_row[i].add(board[i][j])
                mp_col[j].add(board[i][j])
                mp_grid[(i // 3, j // 3)].add(board[i][j])
            
        return True