import random

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_conditions

def check_draw(board):
    return all(all(row) for row in board)

def get_free_positions(board):
    return [(r, c) for r in range(3) for c in range(3) if not board[r][c]]

def player_move(board):
    while True:
        try:
            row = int(input("행 선택 (0, 1, 2): "))
            col = int(input("열 선택 (0, 1, 2): "))
            if board[row][col] == '':
                return row, col
            else:
                print("이미 선택된 자리입니다. 다시 선택해주세요.")
        except (ValueError, IndexError):
            print("잘못된 입력입니다. 다시 시도해주세요.")

def computer_move(board):
    position = random.choice(get_free_positions(board))
    return position

def main():
    board = [['' for _ in range(3)] for _ in range(3)]
    current_player = "X"  # X는 사람, O는 컴퓨터
    while True:
        print_board(board)
        if current_player == "X":
            print("사람 차례")
            row, col = player_move(board)
        else:
            print("컴퓨터 차례")
            row, col = computer_move(board)
            print(f"컴퓨터는 {row}, {col}을 선택했습니다.")
        
        board[row][col] = current_player
        if check_win(board, current_player):
            print_board(board)
            print(f"{current_player}가 이겼습니다!")
            break
        if check_draw(board):
            print_board(board)
            print("무승부입니다!")
            break
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
