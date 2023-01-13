import os
import tweepy

from objects.Logs import Logs as log
from config import *

class TwitterBot():

    REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
    api = None

    def __init__(self) -> None:

      auth = tweepy.auth.OAuthHandler(CONF_TW_CONSUMER_KEY, CONF_TW_CONSUMER_SECRET)
      auth.set_access_token(CONF_TW_ACCESS_TOKEN, CONF_TW_ACCESS_TOKEN_SECRET)

      api = tweepy.API(auth)

      try:
          api.verify_credentials()
          log.msg("TwitterBot (Authentication OK)")
      except:
          log.error("TwitterBot (Error during authentication)")
          quit()

      self.api = api

      pass

    def publish(self, frames):

        try:

          media_ids = []

          for filename in frames:
              res = self.api.media_upload(CONF_PATH_FOLDER_FRAMES + filename)
              media_ids.append(res.media_id)

          f_status = open(CONF_PATH_FILE_CURRENT_VIDEO_META, 'r')
          status = f_status.read()
          f_status.close()

          # Clean file to not upload until the next 
          f_clean = open(CONF_PATH_FILE_CURRENT_VIDEO_META, 'w')
          f_clean.write("")
          f_clean.close()

          self.api.update_status(status=status,media_ids=media_ids)

          log.msg('publish (Images published)')
          return True

        except:
          log.error("publish (Images can't be published)")
          return False
