
import argparse # https://machinelearningmastery.com/command-line-arguments-for-your-python-script/
parser = argparse.ArgumentParser()
parser.add_argument("--folder", help="folder path of video to process")
args = parser.parse_args()
config = vars(args)

import os
initial_path = os.getcwd()
os.chdir(config['folder'])

# run the process
import utils as U
U.step2_automatic_captioning_process()

os.chdir(initial_path)




