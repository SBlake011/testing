# Simple Tic-Tac-Toe game with AI using minimax algorithm

import random
from typing import List, Optional

PLAYER = "X"
AI = "O"
EMPTY = " "

WIN_COMBINATIONS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),             # diagonals
]

def display_board(board: List[str]) -> None:
    print("\n".join([
        f" {board[0]} | {board[1]} | {board[2]} ",
        "---+---+---",
        f" {board[3]} | {board[4]} | {board[5]} ",
        "---+---+---",
        f" {board[6]} | {board[7]} | {board[8]} ",
    ]))


def check_win(board: List[str]) -> Optional[str]:
    for a, b, c in WIN_COMBINATIONS:
        if board[a] == board[b] == board[c] != EMPTY:
            return board[a]
    if EMPTY not in board:
        return "tie"
    return None


def available_moves(board: List[str]) -> List[int]:
    return [i for i, spot in enumerate(board) if spot == EMPTY]


def minimax(board: List[str], player: str) -> int:
    winner = check_win(board)
    if winner == AI:
        return 1
    if winner == PLAYER:
        return -1
    if winner == "tie":
        return 0

    moves = available_moves(board)
    if player == AI:
        best_score = -float("inf")
        for move in moves:
            board[move] = AI
            score = minimax(board, PLAYER)
            board[move] = EMPTY
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for move in moves:
            board[move] = PLAYER
            score = minimax(board, AI)
            board[move] = EMPTY
            best_score = min(best_score, score)
        return best_score


def ai_move(board: List[str]) -> int:
    moves = available_moves(board)
    best_score = -float("inf")
    best_move = random.choice(moves)
    for move in moves:
        board[move] = AI
        score = minimax(board, PLAYER)
        board[move] = EMPTY
        if score > best_score:
            best_score = score
            best_move = move
    board[best_move] = AI
    return best_move


def play_game() -> None:
    board = [EMPTY] * 9
    current_player = PLAYER
    while True:
        if current_player == PLAYER:
            display_board(board)
            move = None
            while move not in available_moves(board):
                try:
                    move = int(input("Choose your move (0-8): "))
                except ValueError:
                    continue
            board[move] = PLAYER
        else:
            ai_move(board)
        winner = check_win(board)
        if winner:
            display_board(board)
            if winner == "tie":
                print("It's a tie!")
            else:
                print(f"{winner} wins!")
            break
        current_player = AI if current_player == PLAYER else PLAYER


if __name__ == "__main__":
    play_game()
