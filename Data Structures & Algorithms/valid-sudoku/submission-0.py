class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(len(board)):
            row_set = set()

            for col in board[row]:
                if col != '.':
                    if col in row_set:
                        return False
                    else:
                        row_set.add(col)
        for i in range(len(board)):
            col_set = set()

            for j in range(len(board[i])):
                if board[j][i] != '.':
                    if board[j][i] in col_set:
                        return False
                    else:
                        col_set.add(board[j][i])
        for i in range(len(board)): # length 9
            square_set = set()
            for j in range(3):
                for k in range(3):
                    row = (i//3)*3+j
                    col = (i%3)*3+k
                    if board[row][col] != '.' :
                        if board[row][col] in square_set:
                            return False
                        else:
                            square_set.add(board[row][col])
                    

        return True