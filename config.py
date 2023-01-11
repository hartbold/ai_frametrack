import os
from dotenv import load_dotenv
load_dotenv()

CONF_PATH_FILE_IX = "./current_ix" # str(os.getenv("SERVER_FILE_PATH"))
CONF_PATH_FILE_CURRENT_VIDEO_META = "./current_episode"
CONF_PATH_FILE_VIDEO_URLS = "./all_videos.txt"

CONF_NAME_VIDEO = 'video.mp4'

CONF_IX_FIRST_VIDEO = -1
CONF_IX_FIRST_PAGE = 128

CONF_PATH_FOLDER_VIDEOS = "./videos/" # str(os.getenv("SERVER_FOLDER_VID_PATH"))
CONF_PATH_FOLDER_FRAMES = "./frames/" # str(os.getenv("SERVER_FOLDER_FRAMES_PATH"))

if not os.path.exists(CONF_PATH_FOLDER_VIDEOS):
    os.mkdir(CONF_PATH_FOLDER_VIDEOS, 0o666)

if not os.path.exists(CONF_PATH_FOLDER_FRAMES):
    os.mkdir(CONF_PATH_FOLDER_FRAMES, 0o666)

if not os.path.isfile(CONF_PATH_FILE_IX):
    f = open(CONF_PATH_FILE_IX, 'w')
    f.write(str(CONF_IX_FIRST_PAGE) + "\n" + str(CONF_IX_FIRST_VIDEO))
    f.close()

if not os.path.isfile(CONF_PATH_FILE_CURRENT_VIDEO_META):
    open(CONF_PATH_FILE_CURRENT_VIDEO_META, 'w').close()

if not os.path.isfile(CONF_PATH_FILE_VIDEO_URLS):
    open(CONF_PATH_FILE_VIDEO_URLS, 'w').close()