import os

def hello():
    return "<h1>Hi! I'm {}!</h1>".format(os.environ['HOSTNAME'])
