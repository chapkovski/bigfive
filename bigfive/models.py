from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from radiogrid import RadioGridField

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'bigfive'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass



ROWS = (
    (1, "Extraverted, enthusiastic"),
    (2, "Critical, quarrelsome"),
    (3, "Dependable, self-disciplined"),
    (4, "Anxious, easily upset"),
    (5, "Open to new experiences, complex"),
    (6, "Reserved, quiet"),
    (7, "Sympathetic, warm"),
    (8, 'Disorganized, careless'),
    (9, 'Calm, emotionally stable'),
    (10, 'Conventional, uncreative'),
)

VALUES = (
    (1, "Disagree strongly"),
    (2, "Disagree moderately"),
    (3, "Disagree a little"),
    (4, "Neither agree nor Disagree"),
    (5, "Agree a little"),
    (6, "Agree moderately"),
    (7, "Agree strongly"),
)

AGE_CHOICES =(
    (1, "<20"),
    (2, "21-30"),
    (3, "31-40"),
    (4, "41-50"),
    (5, "51-60"),
    (6, ">60"),
)
class Player(BasePlayer):
    age = models.PositiveIntegerField(verbose_name='What is your age?',
                                        choices=AGE_CHOICES,
                                        initial=None,
                                        widget=widgets.RadioSelect)
    gender = models.CharField(initial=None,
                                choices=['Male', 'Female'],
                                verbose_name='What is your gender?',
                                widget=widgets.RadioSelect())
    bigfive = RadioGridField(rows=ROWS, values=VALUES, require_all_fields=True,
    verbose_name='I see myself as',)
