import tictactoe as game


def test_check_win_rows():
    board = [game.PLAYER, game.PLAYER, game.PLAYER,
             game.EMPTY, game.EMPTY, game.EMPTY,
             game.EMPTY, game.EMPTY, game.EMPTY]
    assert game.check_win(board) == game.PLAYER


def test_check_tie():
    board = [game.PLAYER, game.AI, game.PLAYER,
             game.PLAYER, game.AI, game.AI,
             game.AI, game.PLAYER, game.PLAYER]
    assert game.check_win(board) == "tie"


def test_ai_move_wins():
    board = [game.AI, game.PLAYER, game.PLAYER,
             game.PLAYER, game.AI, game.EMPTY,
             game.EMPTY, game.EMPTY, game.EMPTY]
    move = game.ai_move(board)
    assert board[move] == game.AI
    assert game.check_win(board) == game.AI
