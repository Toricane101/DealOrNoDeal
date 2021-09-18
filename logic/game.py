from .variables import game_start_embed

class Game:
    def __init__(self, ctx, name):
        self.ctx = ctx
        self.name = name
    
    def start_game(self):
        gse = game_start_embed(self.name)
        print(gse.description)