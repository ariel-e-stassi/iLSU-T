
import argparse # https://machinelearningmastery.com/command-line-arguments-for-your-python-script/
parser = argparse.ArgumentParser()
parser.add_argument("--folder", help="folder path of video to process")
parser.add_argument("--verbose", default=False, help="boolean value. When it is True, it shows the inner process of the function")
parser.add_argument("--minimum_duration", default=25, help="integer value. The function filtered out all the periods of no-face detection\
                     with a duration less than 'minimum_duration'. Default: 25.")
parser.add_argument("--fps", default=25, help="frames per second of the video. Default: 25.")

args = parser.parse_args()
config = vars(args)

import os
initial_path = os.getcwd()
os.chdir(config['folder'])


# run the process
import utils as U
U.step1_ROI_video_cropping_process(config['verbose'])
U.step2_automatic_captioning_process(config['verbose'])
U.step3_signer_detection_A_stage(config['verbose']) # at the "A" stage, it is carried out face detection at a frame level, and saved all the frame IDs with no-face detected in a txt file.
U.step3_signer_detection_B_stage(config['verbose'], int(config['minimum_duration']), int(config['fps'])) # at the "B" stage, it is carried out a post-processing of the raw detections, considering a minimum number of frames in each state of detection (signer versus no-signer).

os.chdir(initial_path)  




