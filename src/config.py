import os

if not os.getenv("RUNNING_CONTAINER"):
    from dotenv import load_dotenv
    print("Running on local environment.")
    load_dotenv()

# Be sure to replace your-user-id with your own user ID or one of an authenticating user
# You can find a user ID by using the user lookup endpoint

target_user_id = 542819818
initial_tweet_id = "000000"

user_id = os.getenv("USER_ID")
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")