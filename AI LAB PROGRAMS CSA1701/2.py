n = int(input("Enter number of queens: "))

board = [-1] * n

for row in range(n):
    for col in range(n):
        if all(board[i] != col and abs(board[i] - col) != row - i
               for i in range(row)):
            board[row] = col
            break

for row in board:
    print("." * row + "Q" + "." * (n - row - 1))
