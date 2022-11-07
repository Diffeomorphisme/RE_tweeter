import config
import get_tweets
import tweet
import lookup_quote_tweet
from scheduler import Scheduler


scheduler = Scheduler()


def fetch_and_retweet():
    target_user_id = config.target_user_id
    user_id = config.user_id
    newest_tweet_id = config.initial_tweet_id

    current_tweet_id = newest_tweet_id
    print("Ongoing")
    newest_tweet_id, genuine_tweet = get_tweets.fetch_most_recent_tweet_id(target_user_id=target_user_id)
    if current_tweet_id != newest_tweet_id:
        print(f"New tweet: {newest_tweet_id}")
        if lookup_quote_tweet.main(tweet_id=newest_tweet_id, user_id=user_id):
            print(f"Tweet not yet quoted.")
            tweet.retweet(tweet_id=newest_tweet_id, genuine_tweet=genuine_tweet)
            print(f"Tweet now quoted.")
            scheduler.add_task(fetch_and_retweet)
            return
        print(f"Tweet already quoted.")
        scheduler.add_task(fetch_and_retweet)
        return
    print(f"No new tweet.")
    scheduler.add_task(fetch_and_retweet)
    return

print("Lets go")
scheduler.add_task(fetch_and_retweet)

while True:
    pass
