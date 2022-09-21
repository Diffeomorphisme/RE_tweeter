import config
import get_tweets
import retweet
from thread import RepeatedTimer

target_user_id = config.target_user_id
newest_tweet_id = config.initial_tweet_id


def fetch_and_retweet():
    global newest_tweet_id
    current_tweet_id = newest_tweet_id
    newest_tweet_id = get_tweets.fetch_most_recent_tweet_id(target_user_id)
    if current_tweet_id != newest_tweet_id:
        retweet.retweet(newest_tweet_id)


rt = RepeatedTimer(60, fetch_and_retweet)