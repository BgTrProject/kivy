# importing libraries and packages
import snscrape.modules.twitter as sntwitter
import pandas as pd
import os
# Query by text search
# Setting variables to be used in format string command below
tweet_count = 500
text_query = "Kavala"
user = "dw_turkce"
since_date = "2021-06-01"
until_date = "2022-02-04"
near ="Istanbul"
lang="tr"

# Using OS library to call CLI commands in Python
os.system('snscrape --jsonl --progress --max-results {} --since {} twitter-search "{} until:{} lang:{} near:{}"> '
          'text-query-tweets.json'.format(tweet_count, since_date, text_query, until_date, lang, near))

tweets_df2 = pd.read_json('text-query-tweets.json', lines=True)