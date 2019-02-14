from praw.models import Comment, Submission
import re

def planeText(s):
    s = re.sub("[^\x00-\x7F]",'',s) #remove non asci characters
    s = re.sub("(?<=\]\()([^\)]+)(?=\))",'',s) #Strip Reddit links
    s = s.translate(str.maketrans('\t\n\v\f\r','     ')) #change all whitespace characters t0 ' '
    s = re.sub("\/u\/(\S+)",'',s) #remove /u/username TODO: make these remove the entire name
    s = re.sub("\/r\/(\S+)",'',s) #remove /r/subreddit
    s = s.translate(str.maketrans('','',"`~!@#$%^&*()_+={}|[]\:;<>?,./1234567890+'")) #remove most punctuation and number
    s = re.sub("((?<=\s)(\"))|((\")(?=\s))",'',s) #strip quotes
    s = re.sub("((?<=\W)-)|(-(?=\W))",'',s) # strip trailing or leading '-'
    return ' '.join(s.split()) #removed extra whitespace

def postWords(post):
    if not isinstance(post,Submission):
        raise Exception("expected praw.models.Submission, got {}".format(type(post)))
    
    wordList=postText(post).split()
    return {word.lower():wordList.count(word) for word in set(wordList)}

def commentWords(comment):
    if not isinstance(comment,Comment):
        raise Exception("expected praw.models.Comment, got {}".format(type(comment)))
    
    wordList=commentText(comment).split()
    return {word.lower():wordList.count(word) for word in set(wordList)}

postText= lambda post: planeText(post.title)+' '+planeText(post.selftext)

commentText = lambda comment: planeText(comment.body)