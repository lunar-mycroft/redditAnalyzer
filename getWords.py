from praw.models import Comment, Submission
import re

def planeText(s):
    s=s.translate(str.maketrans('\t\n\v\f\r','     '))
    s=s.replace('/u/','')
    s=re.sub("(?<=\]\()([^\)]+)(?=\))",'',s) #Strip Reddit links
    s=s.translate(str.maketrans('','',"`~!@#$%^&*()_+={}|[]\:;<>?,./1234567890+"))
    s = re.sub("((?<=\s)(\"|'))|((\"|')(?=\s))",'',s) #strip quotes, but not apostrophies
    s = re.sub("((?<=\W)-)|(-(?=\W))",'',s) # strip trailing or leading '-'
    return ' '.join(s.split())

def postWords(post):
    if not isinstance(post,Submission):
        raise Exception("expected praw.models.Submission, got {}".format(type(post)))
    
    wordList=postText(post).split()
    return {word:wordList.count(word) for word in set(wordList)}

def commentWords(comment):
    if not isinstance(comment,Comment):
        raise Exception("expected praw.models.Comment, got {}".format(type(comment)))
    
    wordList=commentText(comment).split()
    return {word:wordList.count(word) for word in set(wordList)}

postText= lambda post: planeText(post.title)+' '+planeText(post.selftext)

commentText = lambda comment: planeText(comment.body)
    
    