import tweepy
from textblob import TextBlob
import csv
import time

import os

# Authentication: set these as environment variables (never commit real keys)
consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
client = tweepy.Client(bearer_token=bearer_token)

# Define Function to Fetch and Save Tweets
def fetch_and_save_tweets(query, filename="tweets.csv"):
    try:
        response = client.search_recent_tweets(query=query, max_results=10)

        # Open CSV file for writing
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Tweet", "Sentiment"])  # Header row

            for tweet in response.data:
                tweet_text = tweet.text

                # Perform Sentiment Analysis
                analysis = TextBlob(tweet_text)
                sentiment = "positive" if analysis.sentiment.polarity > 0 else "negative"

                # Write to CSV file
                writer.writerow([tweet_text, sentiment])

                # Print for debugging (optional)
                print(f"Tweet: {tweet_text}\nSentiment: {sentiment}\n")

                time.sleep(1)  # Avoid hitting rate limits

        print(f"\n✅ Tweets saved to {filename} successfully!")

    except tweepy.TooManyRequests:
        print("🚨 Rate limit exceeded. Waiting for 15 minutes before retrying...")
        time.sleep(900)
        fetch_and_save_tweets(query, filename)

# Execute
fetch_and_save_tweets("Trump")
