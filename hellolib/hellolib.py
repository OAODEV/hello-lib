import os

def hello():
    """ return html saying hello from this hostname """

    greeting = os.environ.get("greeting", "Hi! I'm not sure what to say. :(")
    return greeting
