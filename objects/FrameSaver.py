from config import CONF_NAME_VIDEO, CONF_PATH_FOLDER_FRAMES, CONF_PATH_FOLDER_VIDEOS
import cv2
import os

from moviepy.editor import VideoFileClip
from objects.Logs import Logs as log
# from flask import Flask


class FrameSaver:

    def __init__(self):
        pass

    def save_frames(self):
        v_path = CONF_PATH_FOLDER_VIDEOS + CONF_NAME_VIDEO

        try:
            log.msg("treat_video (Treating: "+v_path+")")
            vid = VideoFileClip(v_path)
            vid.write_images_sequence(CONF_PATH_FOLDER_FRAMES + 'frame_%04d.jpg', 0.008)
            log.msg("treat_video (Frames saved at: "+CONF_PATH_FOLDER_FRAMES+")")

            # self.delete_blurry_images(CONF_PATH_FOLDER_FRAMES)

        except:
            log.error("treat_video (Couldnt retrieve all frames)")

        # Delete video
        try:
            os.remove(v_path)
        except:
            log.error("treat_video (Couldnt delete video)")

    @staticmethod
    def variance_of_laplacian(image):
        return cv2.Laplacian(image, cv2.CV_64F).var()

# Defining the function to delete the blurry images
    def delete_blurry_images(self, path):
        for file in os.listdir(path):
            image = cv2.imread(os.path.join(path, file))
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            fm = FrameSaver.variance_of_laplacian(gray)
            if fm < 100:
                os.remove(os.path.join(path, file))


""" vidcap = cv2.VideoCapture(videopath)
success, image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count, image)
  success, image = vidcap.read()
  count = 1 """


'''
# app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
videopath = './static/01-01.mp4'

vidcap = cv2.VideoCapture(videopath)
success, image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count, image)
  success, image = vidcap.read()
  count = 1

# Analyze the whole video using the OpenAI API
video = openai.Video(videopath)
response = openai.VideoClassify().predict(video=video)
best_frames = response['best_frames']

# Write the best frames to disk using the Python library moviepy 
from moviepy.editor import VideoFileClip
vid = VideoFileClip(videopath)
vid.write_images_sequence('./frames/frame_%04d.jpg', best_frames)
'''
