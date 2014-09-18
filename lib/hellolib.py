import os

def hello():
    """ return html saying hi from this hostname """

    return "<h1>Hi! I'm {}!</h1>".format(os.environ['HOSTNAME'])
