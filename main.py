import json


from praw import Reddit

from utility.getWords import postWords, commentWords
from utility.sigFigs import sigFigs
from utility.markdownTools import markdownTable

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
    ),
    username=config["auth"]["username"],
    password=config["auth"]["password"]
)

print("logged on as", reddit.user.me())

user=reddit.redditor(config["username"])

wordDict={}
with open('words.json','r') as wordFile:
    wordDict=json.load(wordFile)

print("Finished loading dataset")

numPosts=0
numComments=0



for comment in user.comments.new(limit=None):
    numComments+=1
    for word, n in commentWords(comment).items():
        if word in wordDict:
            wordDict[word][0]+=n
        else:
            wordDict[word]=[n,0]

print("Finished processing comments")

for post in user.submissions.new(limit=None):
    numPosts+=1
    for word, n in postWords(post).items():
        if word in wordDict:
            wordDict[word][0]+=n
        else:
            wordDict[word]=[n,0]

print("finished processing posts")

sums=sum(map(lambda tup: tup[0],wordDict.values())),sum(map(lambda tup: tup[1],wordDict.values()))

inBoth={word:nums for word,nums in wordDict.items() if nums[1]>0 and nums[0]>0}
onlyYou={word:nums for word,nums in wordDict.items() if nums[0]>0 and nums[1]<=0}
neverUsed={word:nums for word,nums in wordDict.items() if nums[1]>0 and nums[0]<=0}
print(len(neverUsed))
print(len(onlyYou))

inBothTable=[ ['Word','Relative frequency^1']]
inBothTable.extend(
    [[word, "{:,}".format(sigFigs((nums[0]/nums[1])*(sums[1]/sums[0]),4))]
        for word, nums in sorted(
            sorted(inBoth.items(),key=lambda t:t[1][1],reverse=True), 
            key=lambda t: t[1][0]/t[1][1],
            reverse=True
        )[:100]]
    )
onlyYouTable=[["Word", "Frequency"]]
onlyYouTable.extend(
    [[word, "{:,}".format(sigFigs(nums[0]/sums[0],4))]
        for word, nums in sorted(
            onlyYou.items(),
            key=lambda t: t[1][0],
            reverse=True
        )[:100]]
    )
neverUsedTable=[["Word", "Frequency"]]
neverUsedTable.extend(
    [ [word, "{:,}".format(sigFigs(nums[1]/sums[1],4))]
        for word,nums in sorted(
            neverUsed.items(),
            key=lambda t:t[1][1],
            reverse=True 
        )[:100]]
    )

msgTemplate=""

with open("messageTemplate.md",'r') as msgTemplateFile:
    msgTemplate=msgTemplateFile.read()



msg=msgTemplate.format(
    username=config["username"],
    numWords=sums[0],
    numPosts=numPosts,
    numComments=numComments,
    numUnique=len(onlyYou)+len(inBoth),
    numNotInDS=len(onlyYou),
    numNotUsed=len(neverUsed),
    table1=markdownTable(inBothTable),
    table2=markdownTable(onlyYouTable),
    table3=markdownTable(neverUsedTable)
    )

reddit.user.me().message("Word frequency analysis for /u/{}".format(config["username"]),msg)

print("Message sent to /u/{}".format(reddit.user.me()))