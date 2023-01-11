from config import CONF_PATH_FOLDER_FRAMES
from objects.TwitterBot import TwitterBot
from objects.VideoScrapper import VideoScrapper
from objects.FrameSaver import FrameSaver
import os

'''

'''

n_frames = os.listdir(CONF_PATH_FOLDER_FRAMES)

tw = TwitterBot()

if len(n_frames) > 0:

  tw.publish()

else:
  vs = VideoScrapper()
  vs.save_video()

  vt = FrameSaver()
  vt.save_frames()

  # Todo OK - actualizamos el fichero para leer el próximo video
  vs.update_file()

  tw.publish()

