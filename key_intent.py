import requests
from alexa_skill.intents import BaseIntents


class JokeIntents(BaseIntents):
    @property
    def mapper(self):
        return {'random_joke': self.random_joke}

    def random_joke(self):return self.response('Kyle sucks'), True