from uno import UnoGame, COLORS
import random

class UnoEnv():
    """
    Description:
        Card game Uno.
    Source:
        Python version by bennuttall.
    Observation:
        Type:
        Num	Observation
        0-107	Cards in hand (one-hot)
        108-215 *7	Last 7 cards played (one-hot)

    Actions:
        Type:
        Num	Action
        0-107	Any of player's hand
        108-111	Declaring new color


    Reward:
        Reward is +1 for each number card, skip, reverse, +2 for draw two, wild, +4 for wild+4, +points won at the end of a game

    Episode Termination:
        Game over
    """
    def __init__(self):
        self.game = UnoGame(5)
