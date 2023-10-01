import chess
from chess import Board, Move

board: Board = chess.Board()

print(board.fen())

# for move in board.legal_moves:
#     print(move)
