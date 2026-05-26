class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            adict = {}
            col_dict = {}
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    adict[board[i][j]] = 1 + adict.get(board[i][j], 0)
                    if adict[board[i][j]] > 1:
                        return False

                if board[j][i] != ".":
                    col_dict[board[j][i]] = 1 + col_dict.get(board[j][i], 0)
                    if col_dict[board[j][i]] > 1:
                        return False
          
        for i in range(len(board)):
            dict3 = {}
            for j in range(3):
                for k in range(3):
                    row = i//3 * 3 + j
                    col = i%3 * 3 + k
                    if board[row][col] != ".":
                        dict3[board[row][col]] = 1 + dict3.get(board[row][col], 0)
                        if dict3[board[row][col]] > 1:
                            return False
        return True
