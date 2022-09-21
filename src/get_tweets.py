import requests
import json
import config

bearer_token = config.bearer_token


def create_url(target_user_id: str):
    # Replace with user ID below
    return "https://api.twitter.com/2/users/{}/tweets".format(target_user_id)


def get_params():
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    return {"tweet.fields": "created_at"}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserTweetsPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.request("GET", url, auth=bearer_oauth, params=params)
    #print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def fetch_most_recent_tweet_id(target_user_id: str):
    url = create_url(target_user_id)
    params = get_params()
    json_response = connect_to_endpoint(url, params)
    return json_response["meta"]["newest_id"]

if __name__ == "__main__":
    fetch_most_recent_tweet_id()