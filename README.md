# redditAnalyzer

A PRAW tutorial project for HackSU

##Requirements

- [Python 3](https://www.python.org/downloads/)
- A reddit account.  Accounts are free to create and don't require email or other details.  

## Installing 

The only dependency is PRAW (Python Reddit API Wrapper).  If you have _only_ python 3 and PIP installed, all you have to do is run the following on a admin terminal/powershell:
```pip install praw```

If you have python 3 and python 2 installed, please this command instead:
```pip3 install praw```

## Reddit app setup:

While logged on to reddit with the account you wish to use, [open your reddit app settings](https://www.reddit.com/prefs/apps/).  Click the "create app" button, and fill out the form as follows:

- name: can be anything you like, but I suggest something descriptive like "Reddit User Word Frequency Analyzer"
- type: this is a script.  Don't worry about the "will only have access to developer accounts" part for now, that only applies to things that require authorization.  You can still read other users posts and comments.
- description: this should be fairly self explanatory.
- about url: can be left blank
- redirect url: we won't be using this, so set it to http://127.0.0.1:65010/authorize_callback

Now that you've created your app, you need to get your client_id and client_secret.  The client_id is the string under your app's name and "personal use script".  Your client_secret is labeled "secret" when you click the "edit" button on the bottom left corner of your app.  You will need both.  Copy exampleConfig.json and rename it to "config.json", then paste the two strings into the relevant fields in that file.  While you're here, enter the username you wish to analyze under "username" (if you don't have much of a comment/post history, feel free to leave that as my username, lunar_mycroft) and the username of your own account under auth->username (you can also enter your reddit password to auth->password now, but that won't be needed until later) and user_agent->author.  It isn't required, but it would probably be advisable to change the user_agent->name field to match your app name at this stage as well.