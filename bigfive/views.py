from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Demographics(Page):
    form_model = models.Player
    form_fields = ['age',
                   'gender']

class BigFive(Page):
    form_model = models.Player
    form_fields = ['bigfive']


page_sequence = [
    Demographics,
    BigFive,
]
