from thread import RepeatedTimer

import config
import get_tweets
import retweet
import lookup_quote_tweet

target_user_id = config.target_user_id
user_id = config.user_id
newest_tweet_id = config.initial_tweet_id


def fetch_and_retweet():
    global newest_tweet_id
    current_tweet_id = newest_tweet_id
    newest_tweet_id, genuine_tweet = get_tweets.fetch_most_recent_tweet_id(target_user_id)
    """
    Good idea to check whether the tweet has been retweeted/quoted 
    by looking at the list of people that have retweeted/quoted it
    """
    if current_tweet_id != newest_tweet_id:
        print(f"New tweet: {newest_tweet_id}")
        if lookup_quote_tweet.main(tweet_id=newest_tweet_id, user_id=user_id):
            print(f"Tweet not yet quoted.")
            retweet.retweet(newest_tweet_id, genuine_tweet)
            print(f"Tweet now quoted.")
        print(f"Tweet already quoted.")
        return
    print(f"No new tweet.")
    return

rt = RepeatedTimer(60, fetch_and_retweet)
