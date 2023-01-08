from objects.TwitterBot import TwitterBot
from objects.VideoScrapper import VideoScrapper
from objects.FrameSaver import FrameSaver
import os

from dotenv import load_dotenv
load_dotenv()

envars = {
  'f_ix' : str(os.getenv("SERVER_FILE_PATH")),
  'v_folder' : str(os.getenv("SERVER_FOLDER_VID_PATH")),
  'f_folder' : str(os.getenv("SERVER_FOLDER_FRAMES_PATH"))
}

'''

'''

n_frames = os.listdir(envars['f_folder'])

tw = TwitterBot()

if len(n_frames) > 0:

  tw.publish()

else:
  vs = VideoScrapper(envars['f_ix'], envars['v_folder'])
  vs.save_video()

  vt = FrameSaver(envars['v_folder'], envars['f_folder'])
  vt.save_frames()

  # Todo OK - actualizamos el fichero para leer el próximo video
  vs.update_file()

  tw.publish()

