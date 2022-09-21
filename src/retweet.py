from requests_oauthlib import OAuth1Session
import os
import json
import config


def retweet(tweet_id: str):
    consumer_key = config.consumer_key
    consumer_secret = config.consumer_secret
    access_token = config.access_token
    access_token_secret = config.access_token_secret

    id = config.user_id

    # You can replace the given Tweet ID with your the Tweet ID you want to Retweet
    # You can find a Tweet ID by using the Tweet lookup endpoint
    #payload = {"tweet_id": "1570870783463026688"}
    payload = {"tweet_id": tweet_id}

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    # Making the request
    response = oauth.post(
        "https://api.twitter.com/2/users/{}/retweets".format(id), json=payload
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))

    # Saving the response as JSON
    json_response = response.json()
    print(json.dumps(json_response, indent=4, sort_keys=True))

