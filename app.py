from config import CONF_PATH_FOLDER_FRAMES
from objects.TwitterBot import TwitterBot
from objects.VideoScrapper import VideoScrapper
from objects.FrameManager import FrameManager
from objects.Logs import Logs as log


tw = TwitterBot()
vt = FrameManager()

frames_tupload = vt.get_next_frames()

if len(frames_tupload) <= 0:
  # No more frames, leemos un nuevo video
  log.msg('app (No more frames)')

  vs = VideoScrapper()
  video_path = vs.save_video()
  vt.save_frames(video_path)

  frames_tupload = vt.get_next_frames()
  vs.update_file()
else:
  log.msg('app (Still frames)')

# Publish
result = tw.publish(frames_tupload)

if result:
  for i in frames_tupload:
    vt.delete_frame(i)

