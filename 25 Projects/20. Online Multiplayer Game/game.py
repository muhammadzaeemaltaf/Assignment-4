class Game:
    def __init__(self, id):
        self.p1Went = False  # Corrected typo
        self.p2Went = False  # Corrected typo
        self.ready = False
        self.id = id
        self.move = [None, None]  # Initialize moves for both players
        self.win = [0, 0]
        self.ties = 0

    def get_player_move(self, p):
        return self.move[p]

    def play(self, player, move):
        self.move[player] = move
        if player == 0:
            self.p1Went = True  # Corrected typo
        else:
            self.p2Went = True  # Corrected typo

    def connected(self):
        return self.ready

    def bothWent(self):
        return self.p1Went and self.p2Went  # Corrected typo

    def winner(self):
        if self.move[0] is None or self.move[1] is None:
            return None  # Return None if any player hasn't made a move yet

        p1 = self.move[0].upper()[0]
        p2 = self.move[1].upper()[0]

        winner = -1
        if p1 == "R" and p2 == "S":
            winner = 0
        elif p1 == "S" and p2 == "R":
            winner = 1
        elif p1 == "S" and p2 == "P":
            winner = 0
        elif p1 == "P" and p2 == "S":
            winner = 1
        elif p1 == "P" and p2 == "R":
            winner = 0
        elif p1 == "R" and p2 == "P":
            winner = 1
        elif p1 == p2:
            winner = -1

        return winner

    def reset(self):
        self.p1Went = False  # Corrected typo
        self.p2Went = False  # Corrected typo
