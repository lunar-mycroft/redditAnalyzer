# Reddit Analyzer

A PRAW tutorial project for HackSU

## Goal
By the end of this project, you will have a simple script that analyzes all of your most recent posts and comments an compares the word frequency of your reddit activity to that of general english text (according to [a dataset of the 1/3 million most frequently used english words](http://norvig.com/ngrams/count_1w.txt) by [Peter Norvig](http://norvig.com/ngrams/)

# Settup

## Requirements

- [Python 3](https://www.python.org/downloads/)
- A reddit account.  Accounts are free to create and don't require email or other details.  

## Installing libraries

The only dependency is PRAW (Python Reddit API Wrapper).  If you have _only_ python 3 and PIP installed, all you have to do is run the following on a admin terminal/powershell:
```pip install praw```

If you have _both_ python 3 and python 2 installed, please run this command instead to ensure you install PRAW for the correct version of python:
```pip3 install praw```

## Reddit app setup:

While logged on to reddit with the account you wish to use, [open your reddit app settings](https://www.reddit.com/prefs/apps/).  Click the "create app" button, and fill out the form as follows:

- name: can be anything you like, but I suggest something descriptive like "Reddit User Word Frequency Analyzer"
- type: this is a script.  Don't worry about the "will only have access to developer accounts", that only applies to things that require authorization.  You can still read other users posts and comments.
- description: this should be fairly self explanatory.
- about url: can be left blank
- redirect url: we won't be using this, so set it to http://127.0.0.1:65010/authorize_callback

## Configuring your script
Now that you've created your app, we need to set up your config file.  A config file isn't needed to make a PRAW script, but its best practices to store this info in a seperate file outside of version control.  Copy exampleConfig.json and rename it to "config.json".  You will need to get your client_id and client_secret.  The client_id is the string under your app's name and "personal use script" your reddit app settings.  Your client_secret is labeled "secret" when you click the "edit" button on the bottom left corner of your app.  Copy-paste the two strings into the relevant fields in that file.  While you're here, enter the username you wish to analyze under "username".  Note this does not have to be the same as the username you are logged on as (if you don't have much of a comment/post history, feel free to leave that as my username, lunar_mycroft) and the username of your own account under auth->username.  Also enter user_agent->name and user_agent->author at this point.  It isn't required, but it would probably be advisable to set it to to match your app name.  Last, enter your reddit password under auth->password (this will be saved in plaintext, so make sure to keep config.json secure.  There are other ways to authenticate with the reddit API which you would use in production, but they're more complicated).  Save the file and close it, we won't need it again.
