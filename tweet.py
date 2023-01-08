import tweepy
import os


# In your terminal please set your environment variables by running the following lines of code.
# export 'CONSUMER_KEY'='<your_consumer_key>'
# export 'CONSUMER_SECRET'='<your_consumer_secret>'

from dotenv import load_dotenv
load_dotenv()

envars = {
  'f_ix' : str(os.getenv("SERVER_FILE_PATH")),
  'v_folder' : str(os.getenv("SERVER_FOLDER_VID_PATH")),
  'f_folder' : str(os.getenv("SERVER_FOLDER_FRAMES_PATH")),

  'tw_public' : str(os.getenv("TW_CON_KEY")),
  'tw_private' : str(os.getenv("TW_CON_KEY_SEC")),
  'tw_tok' : str(os.getenv("TW_ACC_TOK")),
  'tw_tok_private' : str(os.getenv("TW_ACC_TOK_SEC")),
  'tw_cli_id' : str(os.getenv("TW_CLI_ID")),
  'tw_callback' : str(os.getenv("TW_CALLBACK_URL")),
}

CONSUMER_KEY = envars['tw_public']
CONSUMER_SECRET = envars['tw_private']
ACCESS_TOKEN = envars['tw_tok']
ACCESS_TOKEN_SECRET = envars['tw_tok_private']

# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

api.update_status("Test tweet from Tweepy Python", lat='41.4374366', long='2.1811819')




# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# api = tweepy.API(auth)


# oauth2_user_handler = tweepy.OAuth2UserHandler(
#     client_id="Client ID here",
#     redirect_uri="http://ardevol.click",
#     scope=["Scope here", "Scope here"],
#     # Client Secret is only necessary if using a confidential client
#     client_secret="Client Secret here"
# )

# oauth2_user_handler = tweepy.OAuth2UserHandler(
#     client_id=envars['tw_cli_id'],
#     redirect_uri=envars['tw_callback'],
#     scope=["tweet.write"],
# )

# client = tweepy.Client(envars['tw_cli_id'])
# client.create_tweet(text="Texting!")



# status = "Testing!"
# api.update_status(status=status)


# consumer_key = os.getenv("TW_CON_KEY")
# consumer_secret = os.getenv("TW_CON_KEY_SEC")
# # access_token = os.getenv("TW_ACC_TOK")
# # access_token_secret = os.getenv("TW_ACC_TOL_SEC")

# print(
#     "Keys: {} {}".format(consumer_key, consumer_secret)
# )

# # Be sure to add replace the text of the with the text you wish to Tweet. You can also add parameters to post polls, quote Tweets, Tweet with reply settings, and Tweet to Super Followers in addition to other features.
# payload = {"text": "Hello world1!"}

# # Get request token
# request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
# oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

# try:
#     fetch_response = oauth.fetch_request_token(request_token_url)
# except ValueError:
#     print(
#         "There may have been an issue with the consumer_key or consumer_secret you entered."
#     )

# resource_owner_key = fetch_response.get("oauth_token")
# resource_owner_secret = fetch_response.get("oauth_token_secret")
# print("Got OAuth token: %s" % resource_owner_key)

# # Get authorization
# base_authorization_url = "https://api.twitter.com/oauth/authorize"
# authorization_url = oauth.authorization_url(base_authorization_url)
# print("Please go here and authorize: %s" % authorization_url)
# verifier = input("Paste the PIN here: ")

# # Get the access token
# access_token_url = "https://api.twitter.com/oauth/access_token"
# oauth = OAuth1Session(
#     consumer_key,
#     client_secret=consumer_secret,
#     resource_owner_key=resource_owner_key,
#     resource_owner_secret=resource_owner_secret,
#     verifier=verifier,
# )
# oauth_tokens = oauth.fetch_access_token(access_token_url)

# access_token = oauth_tokens["oauth_token"]
# access_token_secret = oauth_tokens["oauth_token_secret"]

# # Make the request
# oauth = OAuth1Session(
#     consumer_key,
#     client_secret=consumer_secret,
#     resource_owner_key=access_token,
#     resource_owner_secret=access_token_secret,
# )

# # Making the request
# response = oauth.post(
#     "https://api.twitter.com/2/tweets",
#     json=payload,
# )

# if response.status_code != 201:
#     raise Exception(
#         "Request returned an error: {} {}".format(response.status_code, response.text)
#     )

# print("Response code: {}".format(response.status_code))

# # Saving the response as JSON
# json_response = response.json()
# print(json.dumps(json_response, indent=4, sort_keys=True))
