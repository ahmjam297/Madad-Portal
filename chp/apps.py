from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class ChpConfig(AppConfig):
    name = 'chp'


class SuitConfig(DjangoSuitConfig):
    layout = 'vertical'
