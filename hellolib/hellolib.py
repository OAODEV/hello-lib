import os

def hello():
    """ return html saying hello from this hostname """

    my_name = os.environ['HOSTNAME'] \
        if "HOSTNAME" in os.environ else "Anonymous"

    return "<h1>Hi! I'm {}!</h1>".format(my_name)
