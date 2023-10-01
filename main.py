import sys
from PyQt5 import QtGui
import chess
import chess.svg
from model.player import Player
from model.victim import Mittens, Stockfish

from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QTimer, Qt, QObject, pyqtSignal


class BoardWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 500, 500)
        self.svgWidget = QSvgWidget(parent=self)
        self.svgWidget.setGeometry(10, 10, 480, 480)

        self.victim: Player = Mittens()
        self.opp: Player = Stockfish()

        self.board = chess.Board()

        self.boardSvg = chess.svg.board(self.board).encode("UTF-8")
        self.svgWidget.load(self.boardSvg)

        self.victimTimer = QTimer(self)
        self.victimTimer.timeout.connect(self.updateVictim)
        self.victimTimer.start(5000)

        self.oppTimer = QTimer(self)
        self.oppTimer.timeout.connect(self.updateOpp)

    def isGameOver(self):
        return self.board.is_game_over()

    def updateVictim(self):
        self.victim.play(self.board)
        self.boardSvg = chess.svg.board(self.board).encode("UTF-8")
        self.svgWidget.load(self.boardSvg)
        self.victimTimer.stop()
        self.oppTimer.start(5000)

    def updateOpp(self):
        self.opp.play(self.board)
        self.boardSvg = chess.svg.board(self.board).encode("UTF-8")
        self.svgWidget.load(self.boardSvg)
        self.oppTimer.stop()
        self.victimTimer.start(5000)


def main():
    app = QApplication(sys.argv)
    window = BoardWidget()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
