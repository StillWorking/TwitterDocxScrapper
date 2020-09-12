import tweepy
from docx import Document
import time

document = Document()

#Create a developer account with twitter and get the following:
consumer_key = "your code here"
consumer_secret = "your code here"
access_token = "your code here"
access_token_secret = "your code here"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

#Create array of tweets

tweets = []

#Specify the user who's tweet you are scraping
username = "Username here"

#Total tweets you want
tweet_number = 100

def tweet_to_docx(username, tweet_number):
    try:
        for tweet in api.user_timeline(id=username, count=tweet_number):
            tweets.append((tweet.created_at,tweet.text))
        table = document.add_table(rows=1, cols=2)
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = 'Tweet Time'
        hdr_cells[1].text = 'Tweet Text'
        for tweet_time, tweet_text in tweets:
            row_cells = table.add_row().cells
            row_cells[0].text = str(tweet_time)
            row_cells[1].text = str(tweet_text)
        document.save('tweets.docx')
    except tweepy.TweepError:
        print('Error! Unable to perform')

#Call the function
tweet_to_docx(username,tweet_number)