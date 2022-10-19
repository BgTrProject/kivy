import GetOldTweets3 as got
tweetCriteria = got.manager.TweetCriteria().setQuerySearch('europe refugees')\
                                           .setSince("2015-05-01")\
                                           .setUntil("2015-09-30")\
                                           .setMaxTweets(1)
tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
print(tweet.text)

import snscrape.modules.twitter as sntwitter
import csv
import os
maxTweets = 100
liste=[]
#keyword = 'deprem'
#place = '5e02a0f0d91c76d2' #This geo_place string corresponds to İstanbul, Turkey on twitter.

#keyword = 'covid'
#place = '01fbe706f872cb32' This geo_place string corresponds to Washington DC on twitter.

#Open/create a file to append data to
with open('place_result4.csv', 'w', newline='', encoding='utf8') as csvf:
    csvWriter = csv.writer(csvf)
    csvWriter.writerow(['id', 'date', 'tweet'])
    # csvf.close()


#Use csv writer

# print("csviye yazıldı")

for i,tweet in enumerate(sntwitter.TwitterSearchScraper('deprem + place:5e02a0f0d91c76d2 + since:2020-10-31 until:2020-11-03 -filter:links -filter:replies').get_items()):
# for i, tweet in enumerate(sntwitter.TwitterSearchScraper('deprem +MURATAKDAG1988 + since:2020-10-31 until:2020-11-03 -filter:links -filter:replies').get_items()):
        if i > maxTweets :
            break
        else:
            with open('place_result4.csv', 'a', newline='', encoding='utf8') as csvf:
                csvWriter2=csv.writer(csvf)
                csvWriter2.writerow([tweet.id, tweet.date, tweet.content])
            # liste.append(tweet.content)
        # print(tweet.content)
csvf.close()
# for i in liste:
#     print(i)
