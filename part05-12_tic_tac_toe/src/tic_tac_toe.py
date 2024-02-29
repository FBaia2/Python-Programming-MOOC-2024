def play_turn(game_board: list, x: int, y: int, piece: str):
    if x > 2 or x < 0 or y > 2 or y < 0:
        return False
    u = len(game_board[0] + game_board[1] + game_board[2])
    print(u)
    print(game_board[y][x])
    if game_board[y][x] == "":
        game_board[y][x] = piece
        return True
    else:
        return False




if __name__ == "__main__":
    game_board = [["", "", ""],
                  ["", "", ""],
                  ["", "", ""]]
    print(play_turn(game_board, 3, 0, "X"))
    print(game_board)