REQUESTS = {
    'LaunchRequest': launch_request,
    'IntentRequest': intent_request,
    'SessionEndedRequest': session_ended_request
}


def launch_request():
    return {
        'request': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': 'Welcome to Button Buzzers!'
            }
        },
        'shouldEndSession': False
    }


def intent_request(json):
    pass


def session_ended_request():
    return {
        'request': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': 'Welcome to Button Buzzers!'
            }
        },
        'shouldEndSession': True
    }
