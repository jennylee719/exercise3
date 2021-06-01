# created on Dec 24, 2020
# modified on April 14, 2021
# @author:          Bo Zhao
# @email:           zhaobo@uw.edu
# @website:         https://hgis.uw.edu
# @organization:    Department of Geography, University of Washington, Seattle
# @description:     Search existing tweets
# @reference: https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/twitter-data-in-python/

import tweepy, json, time, csv

# Create a csv file to store the structured data after processing.
csvfile = open("assets/tweets_ko.csv", "w", newline='', encoding="utf-8") # mode a, r, w

# All the fields of each data entry that I want to collect.
fieldnames = ['username', 'userid', 'profile_location', 'created_at', 'text', 'retweet_count', 'source']

# Create a writer to write the structured data to the csv file.
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# Write the header to the csv file
writer.writeheader()


# Apply for your own Twitter API keys at https://developer.twitter.com/en/apply-for-access
consumer_key = "G7KKGGIl4j2DtyOQgmky2tEq7"
consumer_secret = "igunvmbX8AbzYW2IO6DCBGeNWldgvasI7dsZccQCz5Yc6hmfm9"
access_token = "1060074981885804544-upck7DHHY5o4JVyMaiizrKholwXdjD"
access_token_secret = "C7NcBdtupMqVHL1CT9GWBafdCdgwso2copaXctltDOHb2"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Define the search term and the date_since date as variables
search_words = "코로나"

# read the Twitter API document to look for other ways to customize your queries.
# refer to https://developer.twitter.com/en/docs/twitter-api/v1/rules-and-filtering/search-operators
# for example: you can ignore all the retweets by #wildfires -filter:retweets
# Geolocalization: the search operator “near” isn’t available in the API, but there is a more precise way to restrict
# your query by a given location using the geocode parameter specified with the template “latitude,longitude,radius”,
# for example, “47.6138893,-122.3107869,10mi” (capitol hill at Seattle). When conducting geo searches, the search API will first attempt to find Tweets、
# which have lat/long within the queried geocode, and in case of not having success, it will attempt to find Tweets created
# by users whose profile location can be reverse geocoded into a lat/long within the queried geocode, meaning that is possible
# to receive Tweets which do not include lat/long information.

date_since = "2020-05-07"



# Collect tweets
# tweets = tweepy.Cursor(api.search, q=search_words, lang="en", since=date_since).items(100)
tweets = tweepy.Cursor(api.search, q=search_words, lang="ko", since=date_since).items(200)

# Iterate and print tweets
for tweet in tweets:
    row = {
        'username': tweet.author.name,
        'userid': tweet.author.id,
        'profile_location': tweet.author.location,
        'created_at': str(tweet.author.created_at),
        'text': tweet.text,
        'retweet_count': tweet.retweet_count,
        'source': tweet.source,


    }
    writer.writerow(row)
    print(row)



csvfile.close()
# notify the completion of the program in the console.
print("finished")