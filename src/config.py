import os

if not os.getenv("RUNNING_CONTAINER"):
    from dotenv import load_dotenv
    print("Running on local environment.")
    load_dotenv()

target_user_id = 542819818
initial_tweet_id = "000000"

user_id = os.getenv("USER_ID")
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")
