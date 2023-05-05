class Game:
    @staticmethod
    def toggle(board, i, j):
        board[i][j] = not board[i][j]
        if i > 0:
            board[i-1][j] = not board[i-1][j]
        if i < len(board) - 1:
            board[i+1][j] = not board[i+1][j]
        if j > 0:
            board[i][j-1] = not board[i][j-1]
        if j < len(board[0]) - 1:
            board[i][j+1] = not board[i][j+1]
