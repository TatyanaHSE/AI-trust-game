from otree.api import *

doc = "Instructions"


class C(BaseConstants):
    NAME_IN_URL = 'instructions'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


def progress(page_num, total=10):
    return dict(
        progress_current=page_num,
        progress_total=total,
        progress_percent=round(page_num / total * 100),
    )


class Instructions(Page):
    @staticmethod
    def vars_for_template(player):
        return progress(1)


page_sequence = [Instructions]
