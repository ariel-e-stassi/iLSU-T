
import argparse # https://machinelearningmastery.com/command-line-arguments-for-your-python-script/
parser = argparse.ArgumentParser()
parser.add_argument("--folder", default=None, help="folder path of video to process")
parser.add_argument("--periods", default=1, help="(optional, int value) number of periods of time to segment at first, and then crop independently")

args = parser.parse_args()
config = vars(args)

import os
initial_path = os.getcwd()
os.chdir(config['folder'])
periods = int(config['periods'])
print('here', periods)

# run the process
import utils as U
U.step1_ROI_video_cropping_process(periods)

 





