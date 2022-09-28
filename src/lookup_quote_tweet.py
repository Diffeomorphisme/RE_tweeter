import requests
import config


def auth():
	return config.bearer_token


def create_url(tweet_id):
	# Replace with Tweet ID below

	return "https://api.twitter.com/2/tweets/{}/quote_tweets".format(tweet_id)


def get_params(next_token=None):
	# Tweet fields are adjustable.
	# Options include:
	# attachments, author_id, context_annotations,
	# conversation_id, created_at, entities, geo, id,
	# in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
	# possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
	# source, text, and withheld
	if next_token:
		return {"tweet.fields": "created_at,author_id,referenced_tweets", "pagination_token": f"{next_token}"}
	return {"tweet.fields": "created_at,author_id,referenced_tweets"}


def create_headers(bearer_token):
	headers = {"Authorization": "Bearer {}".format(bearer_token)}
	return headers


def connect_to_endpoint(url, headers, params):
	response = requests.request("GET", url, headers=headers, params=params)
	if response.status_code != 200:
		raise Exception("Request returned an error: {} {}".format(response.status_code, response.text))
	return response.json()


def main(tweet_id, user_id=config.user_id, next_token=None):
	bearer_token = auth()
	url = create_url(tweet_id)
	headers = create_headers(bearer_token)
	params = get_params(next_token)
	json_response = connect_to_endpoint(url, headers, params)
	for tweet in json_response["data"]:
		if tweet["author_id"] == user_id:
			return True
	if "next_token" in json_response["meta"].keys():
		next_token = json_response["meta"]["next_token"]
	main(tweet_id=tweet_id,user_id=user_id, next_token=next_token)
	return False


if __name__ == "__main__":
	main(1573803531747876867)

