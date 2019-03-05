import json

from praw import Reddit

from utility.getWords import postWords, commentWords

config = {}
with open('config.json', 'r') as configFile:
    config=json.load(configFile)
print("Finished loading config")

wordDict = {}
with open('words.json', 'r') as wordFile:
    wordDict = json.load(wordFile)
print("Finished loading dataset")

reddit = Reddit(
    client_id = config['client_id'],
    client_secret = config['client_secret'],
    user_agent = "{}:{}:{} (by {})".format(
        config['user_agent']['platform'],
        config['user_agent']['name'],
        config['user_agent']['version'],
        config['user_agent']['author']
    ),
    username = config["auth"]["username"],
    password = config["auth"]["password"]
)

print("logged on as", reddit.user.me())

user = reddit.redditor(config["username"])

numPosts = 0
numComments = 0

for comment in user.comments.new(limit=None):
    numComments += 1
    for word, n in commentWords(comment).items():
        if word in wordDict:
            wordDict[word][0] += n
        else:
            wordDict[word] = [n,0]
print("Finished loading comments")

for post in user.submissions.new(limit=None):
    numPosts += 1
    for word, n in postWords(post).items():
        if word in wordDict:
            wordDict[word][0] += n
        else:
            wordDict[word] = [n,0]
print("finished loading posts")

print("Number of posts: {}\nNumber of comments: {}".format(numPosts, numComments))