#Summary

Our script analyzed {numWords:,} words from {numPosts:,} (titles and bodies, if present), and {numComments:,} comments.

Overall, /u/{username} used {numUnique:,} different words, {numNotInDS:,} of which were not in the [refrence dataset](http://norvig.com/ngrams/count_1w.txt). /u/{username} never used {numNotUsed:,} out of the dataset of 333,333 words in said dataset.

#Words /u/{username} used more often

Of the words that appeared both in /u/{username}'s comment and the [refrence dataset](http://norvig.com/ngrams/count_1w.txt), these were the 100 they used most:

{table1}

#Words used only by /u/{username}

These are 100 the most frequently used words by /u/{username} that were not in the [refrence dataset](http://norvig.com/ngrams/count_1w.txt):

{table2}

#Words not used by /u/{username}

These are the 100 words most frequently used in the [refrence dataset](http://norvig.com/ngrams/count_1w.txt) that /u/{username} never used:

{table3}

---

^1 Here, relative frequency is the number of times /u/{username} used the word for each time the word occurs in the [refrence dataset](http://norvig.com/ngrams/count_1w.txt).  If /u/{username} uses a word once every 100 words, but the [refrence dataset](http://norvig.com/ngrams/count_1w.txt) uses it only once out of every 200, the relative frequency would be 2.