import tweepy
from textblob import TextBlob
import csv
import time

# Step 1 - Authenticate
consumer_key= 'FEC4oPmCTk8M7pdbuUmz4qoty'
consumer_secret= 'OVN70EYOjnmqsvuNEBXFVPu29cIEJIRjNeI3GoB5EcwwHr4EuA'
bearer_token="AAAAAAAAAAAAAAAAAAAAAKyt0AEAAAAAYGvfViU%2B%2B1LGTd1M8IWmWZ8c2wE%3D45GQjF0lcwT54MaTDWMOi9CmSe8qkdhdysqarFOkMIyqz9GBB3"
access_token='885193407139794944-koNzpQfktK2DnAKMu1NYueQZOkppUoa'
access_token_secret='83iRkYffBkELe4RYdsjlIuv0fUY9hl88O4UQgeJ4TpHWs'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
client = tweepy.Client(bearer_token=bearer_token)

# Step 2 - Define Function to Fetch and Save Tweets
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

# Step 3 - Run Function
fetch_and_save_tweets("Trump")