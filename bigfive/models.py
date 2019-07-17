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
    bigfive = {'Extraversion': [0, 5],
               'Agreeableness': [6, 1],
               'Conscientiousness': [2, 7],
               'Neuroticism': [3, 8],
               'Openness': [4, 9]}


class Subsession(BaseSubsession):
    def vars_for_admin_report(self):
        males = self.player_set.filter(gender=0)

        nmales = males.count()
        females = self.player_set.filter(gender=1)
        nfemales = females.count()
        if nmales > 0:
            men_neuro = sum([i.conversion('Neuroticism') for i in males]) / nmales
        else:
            men_neuro = 0
        if nmales > 0:
            women_neuro = sum([i.conversion('Neuroticism') for i in females]) / nmales
        else:
            women_neuro = 0

        trump_voters = self.player_set.filter(vote=1)
        ntrump_voters = trump_voters.count()
        if ntrump_voters > 0:
            trump_voters_neuro = sum([i.conversion('Neuroticism') for i in trump_voters]) / ntrump_voters
        else:
            trump_voters_neuro = 0
        hillary_voters = self.player_set.filter(vote=0)
        nhillary_voters = hillary_voters.count()
        if nhillary_voters > 0:
            hillary_voters_neuro = sum([i.conversion('Neuroticism') for i in hillary_voters]) / nhillary_voters
        else:
            hillary_voters_neuro = 0
        return {'males': nmales,
                'females': nfemales,
                'trump_voters': ntrump_voters,
                'hillary_voters': nhillary_voters,
                'trump_voters_neuro': trump_voters_neuro,
                'hillary_voters_neuro': hillary_voters_neuro,
                'men_neuro': men_neuro,
                'women_neuro': women_neuro
                }


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
    age = models.IntegerField(label='Please indicate your age', choices=AGE_CHOICES)
    gender = models.IntegerField(choices=[(0, 'Male'), (1, 'Female'), (2, 'Other')], label='What is your gender?')
    vote = models.IntegerField(choices=[(0, 'Hillary Clinton'), (1, 'Donald Trump'), (2, 'Other'), (3, 'Did not vote')],
                               label='Whom did you vote for in presidential elections of 2016?')
    bigfive = RadioGridField(rows=ROWS, values=VALUES, require_all_fields=True,
                             verbose_name='I see myself as', )

    def conversion(self, method):
        i, j = Constants.bigfive[method]
        return 6 - int(self.bigfive[i]) + int(self.bigfive[j])

