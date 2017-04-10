from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Intro(Page):
    def before_next_page(self):
        toguess = random.randint(Constants.minguess, Constants.maxguess)
        self.player.toguess = toguess


class Decision(Page):
    form_model = models.Player
    form_fields = ['guess']

    def before_next_page(self):
        self.player.set_payoff()


class Results(Page):
    ...


page_sequence = [
    Intro,
    Decision,
    Results
]
