
class Pong:
    def __init__(self, max_score):  # Basic init of Pong class
        self.max_score = max_score  # Score Limit to Win the Game
        self.score = [0, 0]  # Score counter, first place for Player 1 and second place for Player 2
        self.turn = 0  # Loop of turns played, if value 0 it's Player 1 turn, if 1 it's Player 2 turn

    def point(self, player):  # If a player scored a Point
        self.score[self.turn] += 1  # Adding Point to Player
        return "Player " + str(self.turn + 1) + " has won the game!" if self.score[
                                                                            self.turn] == self.max_score else "Player " + str(player) + " has missed the ball!"


    def play(self, ball_pos, player_pos):  # Game Play
        player = self.turn + 1  # Keeping track of the player that hit or missed the .play
        self.turn ^= 1  # Making sure that next .play will be the other Player's Turn
        return "Game Over!" if self.max_score in self.score else "Player " + str(
            player) + " has hit the ball!" if player_pos - 3 <= ball_pos <= player_pos + 3 else self.point(player)
        # Verifying if the Game is Won, if the Player Hit the Ball or if the Player Scored a Point.
