from chess import Board
import chess.engine
from model.player import Player


class Mittens(Player):
    def __init__(self):
        self.__engine: chess.engine.SimpleEngine = chess.engine.SimpleEngine.popen_uci(
            r"C:\Users\coolr\Coding\MRKHODE443\ChessBot\model\cage\mittens.exe"
        )

    def play(self, board: Board) -> chess.engine.PlayResult:
        result = self.__engine.play(board, chess.engine.Limit(time=0))
        board.push(result.move)


class Stockfish(Player):
    def __init__(self):
        self.__engine: chess.engine.SimpleEngine = chess.engine.SimpleEngine.popen_uci(
            r"C:\Users\coolr\Coding\MRKHODE443\ChessBot\model\cage\stockfish.exe"
        )

    def play(self, board: Board) -> chess.engine.PlayResult:
        result = self.__engine.play(board, chess.engine.Limit(time=0))
        board.push(result.move)
