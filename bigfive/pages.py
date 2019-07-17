from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class BigFive(Page):
    form_model = 'player'
    form_fields = ['bigfive', ]
    def before_next_page(self):
        print(self.player.bigfive)
    def post(self):
        print(self.request.POST)

        return super().post()

class Q(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'vote']


page_sequence = [
    BigFive,
    Q,
]
