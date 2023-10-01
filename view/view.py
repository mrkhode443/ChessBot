import chess
import chess.svg
from model.player import Player
from model.victim import Mittens, Stockfish

from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QTimer


# Training Widget
class TrainingWidget(QWidget):
    def __init__(self):
        super().__init__()


# Testing Widget
class Testing(QWidget):
    def __init__(self, boardSvg):
        self.setGeometry(100, 100, 500, 500)
        self.svgWidget = QSvgWidget(parent=self)
        self.svgWidget.setGeometry(10, 10, 480, 480)

        # # self.victim: Player = Mittens()
        # # self.opp: Player = Stockfish()

        # self.board = chess.Board()

        self.boardSvg = boardSvg
        self.svgWidget.load(self.boardSvg)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateBoard)
        self.timer.start(5000)

    def updateBoard(self):
        self.svgWidget.load(self.boardSvg)
        self.victimTimer.stop()
        self.oppTimer.start(5000)


class View(QApplication):
    def __init__(self) -> None:
        pass
