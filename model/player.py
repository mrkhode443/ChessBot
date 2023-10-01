from chess import Board


class Player:
    def __init__(self):
        pass

    def play(self, board: Board):
        raise NotImplementedError("Subclass must implement this method")
