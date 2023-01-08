from objects.Logs import Logs as log
import os
import json
from requests_oauthlib import OAuth1Session

from dotenv import load_dotenv
load_dotenv()
envars = {
  'f_folder' : str(os.getenv("SERVER_FOLDER_FRAMES_PATH")),

  'tw_public' : str(os.getenv("TW_CON_KEY")),
  'tw_private' : str(os.getenv("TW_CON_KEY_SEC")),
  'tw_tok' : str(os.getenv("TW_ACC_TOK")),
  'tw_tok_private' : str(os.getenv("TW_ACC_TOK_SEC")),
  'tw_cli_id' : str(os.getenv("TW_CLI_ID")),
  'tw_callback' : str(os.getenv("TW_CALLBACK_URL")),
}

class TwitterBot():

    REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"

    frames_path = ''

    consumer_key = '',
    consumer_secret = ''

    def __init__(self) -> None:

        self.consumer_key = envars['tw_tok']
        self.consumer_secret = envars['tw_tok_private']
        self.frames_path = envars['f_folder']

        pass

    def publish(self):
        # log.msg('')
        return True

