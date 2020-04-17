from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from radiogrid import RadioGridField

author = 'Philipp Chapkovski, chapkovski@gmail.com'

doc = """
Big Five 10-item inventory

Rammstedt, B., & John, O. P. (2007). Measuring personality in one minute or less: A 10-item short version of the 
Big Five Inventory in English and German. Journal of research in Personality, 41(1), 203-212.

https://www.westmont.edu/_academics/departments/psychology/documents/rammstedt_and_john.pdf
"""


class Constants(BaseConstants):
    name_in_url = 'bigfive'
    players_per_group = None
    num_rounds = 1

    bigfive = dict(extraversion=[0, 5],
                   agreeableness=[6, 1],
                   conscientiousness=[2, 7],
                   neuroticism=[3, 8],
                   openness=[4, 9])
    bigfive_categories = bigfive.keys()


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


ROWS = (
    (1, " is reserved"),
    (2, " is generally trusting"),
    (3, " tends to be lazy"),
    (4, " is relaxed, handles stress well"),
    (5, " has few artistic interests"),
    (6, " is outgoing, sociable"),
    (7, " tends to find fault with others"),
    (8, ' does a thorough job'),
    (9, ' gets nervous easily'),
    (10, ' has an active imagination'),
)

VALUES = (
    (1, "Disagree strongly"),
    (2, "Disagree a little"),
    (3, "Neither agree nor Disagree"),
    (4, "Agree a little"),
    (5, "Agree strongly"),
)

AGE_CHOICES = (
    (1, "<20"),
    (2, "21-30"),
    (3, "31-40"),
    (4, "41-50"),
    (5, "51-60"),
    (6, ">60"),
)


class Player(BasePlayer):
    bigfive = RadioGridField(rows=ROWS, values=VALUES, require_all_fields=True,
                             verbose_name='I see myself as', )

    extraversion = models.IntegerField()
    agreeableness = models.IntegerField()
    conscientiousness = models.IntegerField()
    neuroticism = models.IntegerField()
    openness = models.IntegerField()

    def conversion(self, method):
        i, j = Constants.bigfive[method]
        return 6 - int(self.bigfive[i]) + int(self.bigfive[j])
