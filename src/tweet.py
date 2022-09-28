from requests_oauthlib import OAuth1Session
import config


def retweet(tweet_id: str, genuine_tweet: bool):
    consumer_key = config.consumer_key
    consumer_secret = config.consumer_secret
    access_token = config.access_token
    access_token_secret = config.access_token_secret

    id = config.user_id

    if genuine_tweet:
        payload = {"text": "MrAntoineDaniel a just tweeté this: ", "quote_tweet_id": tweet_id}
    else:
        payload = {"text": "MrAntoineDaniel a just retweeté this: ", "quote_tweet_id": tweet_id}

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    # Making the request
    response = oauth.post(
        "https://api.twitter.com/2/tweets",
        json=payload,
    )

    if response.status_code != 200 and response.status_code != 201:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    # print("Response code: {}".format(response.status_code))

    # import json
    # Saving the response as JSON
    # json_response = response.json()
    # print(json.dumps(json_response, indent=4, sort_keys=True))
