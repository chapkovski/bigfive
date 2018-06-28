from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants




class BigFive(Page):
    form_model = 'player'
    form_fields = ['bigfive', 'EA']






page_sequence = [
    BigFive,
]
