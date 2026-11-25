# Tweet Sentiment Analyser (Apr 2025)

A Python script that pulls recent tweets for a search query from the Twitter/X API and labels the sentiment of each one.

**Tools:** Python, Tweepy (Twitter/X API v2), TextBlob

## What it does
- Searches recent tweets for a query with `tweepy.Client.search_recent_tweets`.
- Scores each tweet's polarity with TextBlob and labels it positive or negative.
- Saves the tweets and labels to `tweets.csv`, and waits and retries automatically when the API rate limit is hit.

## Files
- `tweet_sentiment_analyser.py`: the script
- `tweets.csv`: sample output (30 tweets)

## Run it
```bash
pip install tweepy textblob
export TWITTER_CONSUMER_KEY=... TWITTER_CONSUMER_SECRET=... TWITTER_BEARER_TOKEN=... TWITTER_ACCESS_TOKEN=... TWITTER_ACCESS_TOKEN_SECRET=...
python tweet_sentiment_analyser.py
```
