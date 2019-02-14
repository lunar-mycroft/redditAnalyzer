import json


from praw import Reddit

from utility.getWords import postWords, commentWords
from utility.sigFigs import sigFigs

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

user=reddit.redditor(config["username"])

wordDict={}

with open('words.json','r') as wordFile:
    wordDict=json.load(wordFile)

for comment in user.comments.new(limit=None):
    for word, n in commentWords(comment).items():
        if word in wordDict:
            wordDict[word][0]+=n
        else:
            wordDict[word]=[n,0]

for post in user.submissions.new(limit=None):
    for word, n in postWords(post).items():
        if word in wordDict:
            wordDict[word][0]+=n
        else:
            wordDict[word]=[n,0]

sums=sum(map(lambda tup: tup[0],wordDict.values())),sum(map(lambda tup: tup[1],wordDict.values()))

inBoth={word:nums for word,nums in wordDict.items() if nums[1]>0 and nums[0]>0}
onlyYou={word:nums for word,nums in wordDict.items() if nums[0]>0 and nums[1]<=0}
neverUsed={word:nums for word,nums in wordDict.items() if nums[1]>0 and nums[0]<=0}

for word, nums in sorted(sorted(inBoth.items(),key=lambda t:t[1][1],reverse=True), key=lambda t: t[1][0]/t[1][1],reverse=True)[:100]:
    print(word,sigFigs((nums[0]/nums[1])*(sums[1]/sums[0]),4))
print("========")
for word, nums in sorted(onlyYou.items(),key=lambda t:t[1][0],reverse=True)[:100]:
    print(word,nums[0])
print("========")
for word, nums in sorted(neverUsed.items(),key=lambda t:t[1][1],reverse=True)[:100]:
    print(word,nums[1])
print(sums)
print(len(onlyYou),len(inBoth),len(neverUsed))