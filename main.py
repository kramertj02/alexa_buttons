from alexa_skill.intents import BuildInIntents


buildin_intents = BuildInIntents(
    help_message='Say to Alexa: "tell me a joke"',
    not_handled_message="Sorry, I don't understand you. Could you repeat?",
    stop_message='Thanks for playing!',
    cancel_message='Closing button buzzer skill...',
)
