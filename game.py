class CricketGame:
    def __init__(self, game_id):
        self.player1_has_played = False
        self.player2_has_played = False
        self.ready_to_start = False
        self.id = game_id
        self.player_moves = [None, None]
        self.player_wins = [0, 0]
        self.ties = 0
        self.scores = [0, 0]
        self.batting_done = [0, 0]

    def get_player_move(self, player_index):
        """
        :param player_index: [0,1]
        :return: Move
        """
        return self.player_moves[player_index]

    def get_player_score(self, player_index):
        """
        :param player_index: [0,1]
        :return: Move
        """
        return self.scores[player_index]

    def make_move(self, player_index, move):
        self.player_moves[player_index] = move
        if player_index == 0:
            self.player1_has_played = True
        else:
            self.player2_has_played = True

    def are_both_players_ready(self):
        return self.ready_to_start

    def have_both_players_played(self):
        return self.player1_has_played and self.player2_has_played

    def calculate_batsman_score(self, batsman_index, bowler_index, score):
        print("batting_done[0] = ", self.batting_done[0], "and batting_done[0] =", self.batting_done[1])
        batsman_move = self.player_moves[batsman_index]
        bowler_move = self.player_moves[bowler_index]
        print("batsman_move=", batsman_move)
        print("bowler_move=", bowler_move)
        if batsman_move == bowler_move:
            self.batting_done[batsman_index] = 1
            print("batting_done=", batsman_index)
        else:
            score = score + int(batsman_move)
            print("score[batsman_index]", score)
        return score

    def determine_winner(self):
        player1_score = self.scores[0]
        player2_score = self.scores[1]
        print(player1_score)
        print(player2_score)
        if player1_score > player2_score:
            winning_player_index = 0
        elif player1_score < player2_score:
            winning_player_index = 1
        else:
            winning_player_index = -1
        return winning_player_index

    def reset_player_moves(self):
        self.player1_has_played = False
        self.player2_has_played = False