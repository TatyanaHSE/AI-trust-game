from otree.api import *
import random

doc = "Payment information"


class C(BaseConstants):
    NAME_IN_URL = 'payment_info'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    TOLERANCE = 0.05


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    email = models.StringField(label="Enter your email for payment")
    chosen_question = models.StringField(blank=True)
    chosen_model = models.StringField(blank=True)
    prediction_error = models.FloatField(initial=0)
    bonus = models.FloatField(initial=0)
    total_payment = models.FloatField(initial=0)


class Payment(Page):

    @staticmethod
    def vars_for_template(player):
        return dict(
            progress_current=10,
            progress_total=10,
            progress_percent=round(10 / 10 * 100),
        )

    form_model = 'player'
    form_fields = ['email']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        rows = player.participant.vars.get("ai_rows", [])

        if not rows:
            player.chosen_model = "AI Model"
            player.chosen_question = "No data"
            player.prediction_error = 0
            player.bonus = 0
            player.payoff = cu(0)
            player.participant.payoff = cu(0)
            player.total_payment = 0
            return

        chosen_row = rows[0]

        questions = {
            "send": (chosen_row["send"], chosen_row["actual_send"], 1000),
            "r10": (chosen_row["r10"], chosen_row["actual_r10"], 30),
            "r250": (chosen_row["r250"], chosen_row["actual_r250"], 750),
            "r500": (chosen_row["r500"], chosen_row["actual_r500"], 1500),
            "r750": (chosen_row["r750"], chosen_row["actual_r750"], 2250),
            "r1000": (chosen_row["r1000"], chosen_row["actual_r1000"], 3000),
        }

        chosen_question = random.choice(list(questions.keys()))
        prediction, actual, max_value = questions[chosen_question]

        error = abs(prediction - actual)
        tolerance = C.TOLERANCE * max_value

        if error <= tolerance:
            bonus = 1.0
        else:
            bonus = 0.0

        player.chosen_model = "AI Model"
        player.chosen_question = chosen_question
        player.prediction_error = round(error, 2)
        player.bonus = bonus
        player.payoff = cu(bonus)
        player.participant.payoff = cu(bonus)
        player.total_payment = bonus


class ThankYou(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            chosen_model=player.field_maybe_none("chosen_model") or "AI Model",
            chosen_question=player.field_maybe_none("chosen_question") or "—",
            prediction_error=player.field_maybe_none("prediction_error") or 0,
            bonus=player.field_maybe_none("bonus") or 0,
            total_payment=player.field_maybe_none("total_payment") or 0,
            payoff_debug=player.payoff,
            participant_payoff_debug=player.participant.payoff,
        )


page_sequence = [Payment, ThankYou]
