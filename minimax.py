from ... game import Game


class Minimax():
    def play(self, game: Game):
        start = game.get_start_node()
        # 'game.get_max_player()' asks the game how it identifies the MAX player internally.
        # this is just for the sake of generality, so games are free to encode
        # player's identities however they want.
        # (it just so happens to be '1' for MAX, and '-1' for MIN most of the times)
        value, terminal_node = self.minimax(game, start, game.get_max_player())
        return terminal_node

    def minimax(self, game, node, max_player):
        # here we check if the current node 'node' is a terminal node
        terminal, winner = game.outcome(node)

        # if it is a terminal node, determine who won, and return
        # a) the value (-1, 0, 1)
        # b) the terminal node itself, to be able to determine
        #    the path of moves/plies that led to this terminal node
        if terminal:
            if winner is None:
                return 0, node
            elif winner == max_player:
                return 1, node
            else:
                return -1, node

        # TODO, Exercise 3: implement the minimax algorithm recursively here
        # to help you get started, we laid out the basic structure of the
        # algorithm
        if node.player == max_player:
            # you have to remember the best value *and* the best node for the MAX player

            # this is how you get minus infinity as a 'value' (smaller than all other numbers)
            best_value = float('-Inf')
            best_node = None

            # TODO implement logic for MAX player

            for i in game.successors(node):
                eval=self.minimax(game,i,max_player)
                if eval[0] >best_value:
                    best_value=eval[0]
                    best_node=eval[1]
                


            

            return best_value, best_node
        else:
            # you have to remember the best value *and* the best node for the MIN player

            # this is how you get plus infinity as a 'value' (larger than all other numbers)
            best_value = float('Inf')
            best_node = None

            # TODO implement logic for MIN player
            for i in game.successors(node):
                eval=self.minimax(game,i,max_player)
                if eval[0] <best_value:
                    best_value=eval[0]
                    best_node=eval[1]

            return best_value, best_node
