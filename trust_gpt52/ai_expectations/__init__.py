from otree.api import *
import random

doc = "AI expectations in trust game"


class C(BaseConstants):
    NAME_IN_URL = 'ai_expectations'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    MODEL_NAME_DISPLAY = 'AI Model'
    MODEL_NAME_INTERNAL = 'GPT-5.2'

    ACTUAL_RESPONSES = {
        'send': 442.0,
        'r10': 12.5,
        'r250': 339.1,
        'r500': 563.8,
        'r750': 1007.0,
        'r1000': 1581.8,
    }

    MAX_VALUES = {
        'send': 1000,
        'r10': 30,
        'r250': 750,
        'r500': 1500,
        'r750': 2250,
        'r1000': 3000,
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    send = models.IntegerField(min=0, max=1000)
    r10 = models.IntegerField(min=0, max=30)
    r250 = models.IntegerField(min=0, max=750)
    r500 = models.IntegerField(min=0, max=1500)
    r750 = models.IntegerField(min=0, max=2250)
    r1000 = models.IntegerField(min=0, max=3000)

    actual_send = models.FloatField(initial=C.ACTUAL_RESPONSES['send'])
    actual_r10 = models.FloatField(initial=C.ACTUAL_RESPONSES['r10'])
    actual_r250 = models.FloatField(initial=C.ACTUAL_RESPONSES['r250'])
    actual_r500 = models.FloatField(initial=C.ACTUAL_RESPONSES['r500'])
    actual_r750 = models.FloatField(initial=C.ACTUAL_RESPONSES['r750'])
    actual_r1000 = models.FloatField(initial=C.ACTUAL_RESPONSES['r1000'])


class ModelPage(Page):
    form_model = 'player'
    form_fields = ['send', 'r10', 'r250', 'r500', 'r750', 'r1000']

    @staticmethod
    def vars_for_template(player):
        return dict(
            model_name=C.MODEL_NAME_DISPLAY,
            progress_current=3,
            progress_total=10,
            progress_percent=30,
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['ai_rows'] = [
            dict(
                round_number=1,
                model_name=C.MODEL_NAME_INTERNAL,
                display_name=C.MODEL_NAME_DISPLAY,
                send=player.send,
                r10=player.r10,
                r250=player.r250,
                r500=player.r500,
                r750=player.r750,
                r1000=player.r1000,
                actual_send=player.actual_send,
                actual_r10=player.actual_r10,
                actual_r250=player.actual_r250,
                actual_r500=player.actual_r500,
                actual_r750=player.actual_r750,
                actual_r1000=player.actual_r1000,
            )
        ]


page_sequence = [ModelPage]
