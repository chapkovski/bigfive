from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class BigFive(Page):
    form_model = 'player'
    form_fields = ['bigfive']

    def before_next_page(self):
        for i in Constants.bigfive_categories:
            setattr(self.player, i, getattr(self.player, 'conversion')(i))


page_sequence = [
    BigFive,
]
