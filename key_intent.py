import requests
from alexa_skill.intents import BaseIntents


class JokeIntents(BaseIntents):
    @property
    def mapper(self):
        return {'random_joke': self.random_joke}

    def random_joke(self):
        joke_response = requests.get('http://api.icndb.com/jokes/random')
        if joke_response.status_code != 200:
            return self.response('Sorry, I did not find any joke. Please try again'), False

        return self.response(joke_response['value']['joke']), True