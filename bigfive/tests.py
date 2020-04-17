from otree.api import Currency as c, currency_range
from .pages import *
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):

    def play_round(self):
        big_five_keys = [f'bigfive_{i}' for i in range(10)]
        big_five_values = [random.randint(1, 5) for _ in range(10)]
        big_five_answer = dict(zip(big_five_keys, big_five_values))
        yield (BigFive, big_five_answer)
