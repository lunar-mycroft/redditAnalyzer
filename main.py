import json

from praw import Reddit

from getWords import postWords, commentWords

config={}

with open('config.json','r') as configFile:
    config=json.load(configFile)

reddit=Reddit(
    client_id=config['client_id'],
    client_secret=config['client_secret'],
    user_agent="{}:{}:{} (by {})".format(
        config['user_agent']['platform'],
        config['user_agent']['name'],
        config['user_agent']['version'],
        config['user_agent']['author']
    )
)

user=reddit.redditor("tbri")

