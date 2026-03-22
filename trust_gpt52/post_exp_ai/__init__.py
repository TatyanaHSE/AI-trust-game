from otree.api import *

doc = "Post-experiment AI perception survey"


class C(BaseConstants):
    NAME_IN_URL = 'post_exp_ai'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


SCALE_CHOICES = [[i, str(i)] for i in range(1, 11)]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    attn_1 = models.IntegerField(
        choices=SCALE_CHOICES,
        widget=widgets.RadioSelectHorizontal,
        label=""
    )

    use_1 = models.IntegerField(
        choices=SCALE_CHOICES,
        widget=widgets.RadioSelectHorizontal,
        label=""
    )
    use_2 = models.IntegerField(
        choices=SCALE_CHOICES,
        widget=widgets.RadioSelectHorizontal,
        label=""
    )
    use_3 = models.IntegerField(
        choices=SCALE_CHOICES,
        widget=widgets.RadioSelectHorizontal,
        label=""
    )

    def_1 = models.IntegerField(
        choices=SCALE_CHOICES,
        widget=widgets.RadioSelectHorizontal,
        label=""
    )
    def_2 = models.IntegerField(
        choices=SCALE_CHOICES,
        widget=widgets.RadioSelectHorizontal,
        label=""
    )
    def_3 = models.IntegerField(
        choices=SCALE_CHOICES,
        widget=widgets.RadioSelectHorizontal,
        label=""
    )

    ver_1 = models.IntegerField(
        choices=SCALE_CHOICES,
        widget=widgets.RadioSelectHorizontal,
        label=""
    )
    ver_2 = models.IntegerField(
        choices=SCALE_CHOICES,
        widget=widgets.RadioSelectHorizontal,
        label=""
    )
    ver_3 = models.IntegerField(
        choices=SCALE_CHOICES,
        widget=widgets.RadioSelectHorizontal,
        label=""
    )

    acc_1 = models.IntegerField(
        choices=SCALE_CHOICES,
        widget=widgets.RadioSelectHorizontal,
        label=""
    )
    acc_2 = models.IntegerField(
        choices=SCALE_CHOICES,
        widget=widgets.RadioSelectHorizontal,
        label=""
    )
    acc_3 = models.IntegerField(
        choices=SCALE_CHOICES,
        widget=widgets.RadioSelectHorizontal,
        label=""
    )

    mm_1 = models.IntegerField(
        choices=SCALE_CHOICES,
        widget=widgets.RadioSelectHorizontal,
        label=""
    )
    mm_2 = models.IntegerField(
        choices=SCALE_CHOICES,
        widget=widgets.RadioSelectHorizontal,
        label=""
    )
    mm_3 = models.IntegerField(
        choices=SCALE_CHOICES,
        widget=widgets.RadioSelectHorizontal,
        label=""
    )
    mm_4 = models.IntegerField(
        choices=SCALE_CHOICES,
        widget=widgets.RadioSelectHorizontal,
        label=""
    )
    mm_5 = models.IntegerField(
        choices=SCALE_CHOICES,
        widget=widgets.RadioSelectHorizontal,
        label=""
    )


def progress(page_num, total=10):
    return dict(
        progress_current=page_num,
        progress_total=total,
        progress_percent=round(page_num / total * 100),
    )


class PageAttention(Page):
    form_model = 'player'
    form_fields = ['attn_1']

    @staticmethod
    def vars_for_template(player):
        return progress(4)

    @staticmethod
    def error_message(player, values):
        if values['attn_1'] != 7:
            return 'To confirm attention, please select number 7.'


class PageUSE(Page):
    form_model = 'player'
    form_fields = ['use_1', 'use_2', 'use_3']

    @staticmethod
    def vars_for_template(player):
        return progress(5)


class PageDEF(Page):
    form_model = 'player'
    form_fields = ['def_1', 'def_2', 'def_3']

    @staticmethod
    def vars_for_template(player):
        return progress(6)


class PageVER(Page):
    form_model = 'player'
    form_fields = ['ver_1', 'ver_2', 'ver_3']

    @staticmethod
    def vars_for_template(player):
        return progress(7)


class PageACC(Page):
    form_model = 'player'
    form_fields = ['acc_1', 'acc_2', 'acc_3']

    @staticmethod
    def vars_for_template(player):
        return progress(8)


class PageMM(Page):
    form_model = 'player'
    form_fields = ['mm_1', 'mm_2', 'mm_3', 'mm_4', 'mm_5']

    @staticmethod
    def vars_for_template(player):
        return progress(9)


page_sequence = [
    PageAttention,
    PageUSE,
    PageDEF,
    PageVER,
    PageACC,
    PageMM,
]
