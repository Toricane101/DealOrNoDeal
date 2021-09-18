from discord import Embed

colour = 0xfeef92


def game_start_embed(name):
    return Embed(title="Welcome to Deal or No Deal!",
                 description=f"""
Hello! I am Howie Mandel, and welcome to Deal or No Deal!
Please welcome our first contestant, {name}!
""",
                 colour=colour)
