import config
import get_tweets
import retweet
from thread import RepeatedTimer

target_user_id = config.target_user_id
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
        retweet.retweet(newest_tweet_id, genuine_tweet)


rt = RepeatedTimer(60, fetch_and_retweet)
