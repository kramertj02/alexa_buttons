import requests
from alexa_skill.intents import BaseIntents


class JokeIntents(BaseIntents):
    @property
    def mapper(self):
        return {'button_buzzer': self.button_buzzer}

    def button_buzzer(self):
        return self.response('Kyle sucks'), True