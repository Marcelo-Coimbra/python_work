class Gamestats:
    """ Rastreia as estatísticas de Invasão Alienígena """

    def __ini__(self, ai_game):
        """ Inicializa as estatísticas """
        self.setings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """ Inicializa as estatísticas que podem mudar durante o jogo """
        self.ships_left = self.settings.ship_limit