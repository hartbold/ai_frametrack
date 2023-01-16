import os

from objects.Logs import Logs as log
from dotenv import load_dotenv
load_dotenv()

CONF_PATH_FILE_IX = os.environ["PWD"] + "/current_ix" # str(os.getenv("SERVER_FILE_PATH"))
CONF_PATH_FILE_CURRENT_VIDEO_META = os.environ["PWD"] + "/current_episode"
CONF_PATH_FILE_VIDEO_URLS = os.environ["PWD"] + "/all_videos.txt"

CONF_NAME_VIDEO = 'video.mp4'

CONF_IX_FIRST_VIDEO = -1
CONF_IX_FIRST_PAGE = 128

CONF_PATH_FOLDER_VIDEOS = os.environ["TMP"] + "/" # str(os.getenv("SERVER_FOLDER_VID_PATH"))
CONF_PATH_FOLDER_FRAMES = os.environ["PWD"] + "/frames/" # str(os.getenv("SERVER_FOLDER_FRAMES_PATH"))

CONF_TW_CONSUMER_KEY = str(os.getenv("TW_CON_KEY"))
CONF_TW_CONSUMER_SECRET = str(os.getenv("TW_CON_KEY_SEC"))
CONF_TW_ACCESS_TOKEN = str(os.getenv("TW_ACC_TOK"))
CONF_TW_ACCESS_TOKEN_SECRET = str(os.getenv("TW_ACC_TOK_SEC"))

if not os.path.exists(CONF_PATH_FOLDER_VIDEOS):
    log.msg("")
    os.mkdir(CONF_PATH_FOLDER_VIDEOS, 0o777)

if not os.path.exists(CONF_PATH_FOLDER_FRAMES):
    os.mkdir(CONF_PATH_FOLDER_FRAMES, 0o777)

if not os.path.isfile(CONF_PATH_FILE_IX):
    f = open(CONF_PATH_FILE_IX, 'w')
    f.write(str(CONF_IX_FIRST_PAGE) + "\n" + str(CONF_IX_FIRST_VIDEO))
    f.close()

if not os.path.isfile(CONF_PATH_FILE_CURRENT_VIDEO_META):
    open(CONF_PATH_FILE_CURRENT_VIDEO_META, 'w').close()

if not os.path.isfile(CONF_PATH_FILE_VIDEO_URLS):
    open(CONF_PATH_FILE_VIDEO_URLS, 'w').close()