def output_board():
    print("---------")
    for n in range(0, 9, 3):
        print(f"| {' '.join(board[n:n + 3])} |")
    print("---------")

def win_check():
    if (board[0:3].count("X") == 3) or (board[3:6].count("X") == 3) or (board[6:9].count("X") == 3) or (board[::3].count("X") == 3) or (board[::-3].count("X") == 3) or (board[1::3].count("X") == 3) or (board[::4].count("X") == 3 or board[2:7:2].count("X") == 3):
        print("X wins")
        exit()
    elif (board[0:3].count("O") == 3) or (board[3:6].count("O") == 3) or (board[6:9].count("O") == 3) or (board[::3].count("O") == 3) or (board[::-3].count("O") == 3) or (board[1::3].count("O") == 3) or (board[::4].count("O") == 3 or board[2:7:2].count("O") == 3):
        print("O wins")
        exit()
    elif not ' ' in board[0:9]:
        print("Draw")
        exit()

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
output_board()

next_move = "O"

while True:
    try:
        row, col = [int(n) for n in input("Enter the coordinates: ").split()]
    except ValueError:
        print("You should enter numbers!")
        continue
    if not (1 <= row <= 3 and 1 <= col <= 3):
        print("Coordinates should be from 1 to 3!")
        continue

    index = ((3 - col) * 3) + (row - 1)

    if 'X' in board[index] or 'O' in board[index]:
        print("This cell is occupied! Choose another one!")
        continue
    else:
        if next_move == "O":
            board[index] = "X"
            next_move = "X"
        elif next_move == "X":
            board[index] = "O"
            next_move = "O"

    output_board()
    win_check()

