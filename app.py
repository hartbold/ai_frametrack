import os
import cv2
import openai
# from flask import Flask

videopath = './videos/01-01.mp4'

""" vidcap = cv2.VideoCapture(videopath)
success, image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count, image)
  success, image = vidcap.read()
  count = 1 """

from moviepy.editor import VideoFileClip
vid = VideoFileClip(videopath)
vid.write_images_sequence('./frames/frame_%04d.jpg', 0.1)

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

