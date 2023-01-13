# import cv2
import os

from config import *
from moviepy.editor import VideoFileClip
from objects.Logs import Logs as log

class FrameManager:

    def __init__(self):
        pass

    def save_frames(self, v_path):
        
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
            log.msg("treat_video (Video deleted)")
            os.remove(v_path)
        except:
            log.error("treat_video (Couldnt delete video)")

    def get_next_frames(self,n_frames=2):
        frames = os.listdir(CONF_PATH_FOLDER_FRAMES)
        return frames[0:n_frames]

    def delete_frame(self, frame_path):
        os.remove(CONF_PATH_FOLDER_FRAMES+frame_path)
        return True

    # @staticmethod
    # def variance_of_laplacian(image):
    #     return cv2.Laplacian(image, cv2.CV_64F).var()

    # Defining the function to delete the blurry images
    # def delete_blurry_images(self, path):
    #     for file in os.listdir(path):
    #         image = cv2.imread(os.path.join(path, file))
    #         gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #         fm = FrameManager.variance_of_laplacian(gray)
    #         if fm < 100:
    #             os.remove(os.path.join(path, file))