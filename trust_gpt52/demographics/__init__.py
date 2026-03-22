from otree.api import *

doc = """
Participant background survey
"""


class C(BaseConstants):
    NAME_IN_URL = 'demographics'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    age = models.IntegerField(
        label="What is your age?"
    )

    gender = models.StringField(
        label="What is your gender?",
        choices=[
            "Male",
            "Female",
            "Non-binary",
            "Prefer not to say",
        ]
    )

    education = models.StringField(
        label="What is your highest level of education?",
        choices=[
            "High school",
            "Bachelor",
            "Master",
            "PhD",
            "Other",
        ]
    )

    ai_familiarity = models.IntegerField(
        label="How familiar are you with AI tools such as ChatGPT, Claude, DeepSeek, or similar systems?",
        choices=[[i, str(i)] for i in range(1, 11)],
        widget=widgets.RadioSelectHorizontal
    )

    general_trust = models.IntegerField(
        label="Generally speaking, do you think that most people can be trusted?",
        choices=[[i, str(i)] for i in range(1, 11)],
        widget=widgets.RadioSelectHorizontal
    )

    risk_attitude = models.IntegerField(
        label="How willing are you to take risks in general?",
        choices=[[i, str(i)] for i in range(1, 11)],
        widget=widgets.RadioSelectHorizontal
    )

    life_satisfaction = models.IntegerField(
        label="Overall, how satisfied are you with your life these days?",
        choices=[[i, str(i)] for i in range(1, 11)],
        widget=widgets.RadioSelectHorizontal
    )


def progress(page_num, total=10):
    return dict(
        progress_current=page_num,
        progress_total=total,
        progress_percent=round(page_num / total * 100),
    )


class Demographics(Page):
    form_model = 'player'
    form_fields = [
        'age',
        'gender',
        'education',
        'ai_familiarity',
        'general_trust',
        'risk_attitude',
        'life_satisfaction',
    ]

    @staticmethod
    def vars_for_template(player):
        return progress(2)

    @staticmethod
    def error_message(player, values):
        if values['age'] < 16:
            return "Participants younger than 16 years old are not eligible to take part in this study."


page_sequence = [Demographics]
