from os import environ


SESSION_CONFIGS = [
    dict(
        name='ai_trust_experiment',
        display_name='AI Trust Experiment',
        app_sequence = [
    'instructions',
    'demographics',
    'ai_expectations',
    'post_exp_ai',
            'payment_info',
],
        num_demo_participants=10,
    ),
]


SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
    doc="",
)


PARTICIPANT_FIELDS = []
SESSION_FIELDS = []


LANGUAGE_CODE = 'en'


REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False


# Debug
DEBUG = False


# Admin login
ADMIN_USERNAME = 'admin'

# локально будет пароль admin
# на Heroku будет использоваться переменная среды
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD', 'admin')


# Secret key
# локально используется dev-secret-key
# на Heroku берётся из переменной среды
SECRET_KEY = environ.get('OTREE_SECRET_KEY', 'dev-secret-key')


INSTALLED_APPS = ['otree']


DEMO_PAGE_INTRO_HTML = """
<p>AI Trust Experiment</p>
"""
