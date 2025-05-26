import os
import numpy as np
import srt
import datetime 
import subprocess

def step1_ROI_video_cropping_process(periods):
    
    if periods == 1:    
        
        # get the root name and open the ROI txt file:
        root_name = os.getcwd().split('/')[-1]
        ROI_filename = root_name + '_ROI.txt'
        ROI_file = open(ROI_filename,'r')
        
        for row in ROI_file:
            print(row)
    
        
        row = row.split(',')

        # from the file, it is read the upper left corner coordinates (UL_x, UL_y)
        # and the lower right corner coordinates (LR_x, LR_y):

        UL_x, UL_y, LR_x, LR_y = int(row[0]), int(row[1]), int(row[2]), int(row[3])

        # values are formatted into the ffmpeg command for the desired cropping:
        W, H = LR_x - UL_x + 1, LR_y - UL_y + 1

        crop_command_part = 'crop=' + str(W) + ':' + str(H) + ':' + str(UL_x) + ':' + str(UL_y)

        # it is extracted the ROI in an mp4 file WITH and WITHOUT audio track included (ffmpeg provides 2 output files)
        try:
            command = 'ffmpeg -i ' + root_name + '.MXF -vf "' + crop_command_part + ', yadif" -q:v 0 ' + root_name + '_audio.mp4' 
            command += ' -an -vf "' + crop_command_part + ', yadif" -q:v 0 ' + root_name + '_muted.mp4'
            print(command)
            # os.system(command)
            subprocess.call(command, shell=True)
        except FileNotFoundError:
            command = 'ffmpeg -i ' + root_name + '.mxf -vf "' + crop_command_part + ', yadif" -q:v 0 ' + root_name + '_audio.mp4' 
            command += ' -an -vf "' + crop_command_part + ', yadif" -q:v 0 ' + root_name + '_muted.mp4'
            print(command)
            # os.system(command)
            subprocess.call(command, shell=True)  
        finally:
            command = 'ffmpeg -i ' + root_name + '.mp4 -vf "' + crop_command_part + ', yadif" -q:v 0 ' + root_name + '_audio.mp4' 
            command += ' -an -vf "' + crop_command_part + ', yadif" -q:v 0 ' + root_name + '_muted.mp4'
            print(command)
            # os.system(command)
            subprocess.call(command, shell=True)  
    
    elif periods > 1:
        for p in range(1,periods+1):

            # get the root name and open the ROI txt file:
            root_name = os.getcwd().split('/')[-1]
            
            ROI_filename = root_name + '_ROI.txt'
            ROI_file = open(ROI_filename,'r')
            
            periods_filename = root_name + '_periods.txt'
            periods_file = open(periods_filename,'r')
                
            ROI_rows = ROI_file.readlines()
            periods_rows = periods_file.readlines()

            for i in range(int(len(ROI_rows))):   
                
                ROI_row = ROI_rows[i].split(',')
                
                # from the file, it is read the upper left corner coordinates (UL_x, UL_y)
                # and the lower right corner coordinates (LR_x, LR_y):

                UL_x, UL_y, LR_x, LR_y = int(ROI_row[0]), int(ROI_row[1]), int(ROI_row[2]), int(ROI_row[3])

                # values are formatted into the ffmpeg command for the desired cropping:
                W, H = LR_x - UL_x + 1, LR_y - UL_y + 1

                crop_command_part = 'crop=' + str(W) + ':' + str(H) + ':' + str(UL_x) + ':' + str(UL_y)

                period_row = periods_rows[i].split(',')
                period_commant_part = ' -ss ' + period_row[0].strip() + ' -to ' + period_row[1].strip()

                # it is extracted the ROI in an mp4 file WITH and WITHOUT audio track included, considering each defined period 
                # (ffmpeg provides 2 output files per period)
                try:
                    command = 'ffmpeg -i ' + root_name + '.MXF ' + period_commant_part + ' -vf "' + crop_command_part + ', yadif" -q:v 0 ' + root_name + '_' + str(i+1) + '_audio.mp4' 
                    command += period_commant_part + ' -an -vf "' + crop_command_part + ', yadif" -q:v 0 ' + root_name + '_' + str(i+1) + '_muted.mp4'
                    print(command)
                    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
                    # os.system(command)
                    subprocess.call(command, shell=True)
                except FileNotFoundError:
                    command = 'ffmpeg -i ' + root_name + '.mxf ' + period_commant_part + ' -vf "' + crop_command_part + ', yadif" -q:v 0 ' + root_name + '_' + str(i+1) + '_audio.mp4' 
                    command += period_commant_part + ' -an -vf "' + crop_command_part + ', yadif" -q:v 0 ' + root_name + '_' + str(i+1) + '_muted.mp4'
                    print(command)
                    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
                    # os.system(command)
                    subprocess.call(command, shell=True)  
                finally:
                    command = 'ffmpeg -i ' + root_name + '.mp4 ' + period_commant_part + ' -vf "' + crop_command_part + ', yadif" -q:v 0 ' + root_name + '_' + str(i+1) + '_audio.mp4' 
                    command += period_commant_part + ' -an -vf "' + crop_command_part + ', yadif" -q:v 0 ' + root_name + '_' + str(i+1) + '_muted.mp4'
                    print(command)
                    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
                    # os.system(command)
                    subprocess.call(command, shell=True)  

            


def step2_automatic_captioning_process():
    # get the root name    
    root_name = os.getcwd().split('\\')[-1]
        
    # extract the wav track for general purposes a posteriori
    video_filename, audio_filename = root_name + '.mp4"', '"' + root_name + '.wav'
    command = 'ffmpeg -i ' + video_filename + ' -q:a 0 ' + audio_filename
    os.system(command)

    # run the Whisper method
    command = 'whisperx ' + audio_filename + ' --model large-v3 --language es' # warning: Python interpreter must be inside the corresponding virtual environment

def step3_signer_detection_A_stage(verbose):
    # get the root name    
    root_name = os.getcwd().split('/')[-1]

    import cv2 # source: https://www.datacamp.com/tutorial/face-detection-python-opencv

    def detect_bounding_box(vid):
        gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
        if verbose:
            for (x, y, w, h) in faces:
                cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
        return faces

    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    video_filename = root_name + '.mp4'

    video_capture = cv2.VideoCapture(video_filename)
    global_frame_counter = 0

    f = open(video_filename[:-4] + '_frames_sequence_without_signer_A-stage.txt', 'w')
    
    frames_sequence = [] 

    while True:

        result, video_frame = video_capture.read()  # read frames from the video
        if result is False:
            break  # terminate the loop if the frame is not read successfully

        faces = detect_bounding_box(video_frame)  # apply the function we created to the video frame

        if faces == ():
            
            last_frame_without_face = global_frame_counter

            f.write(str(last_frame_without_face) + '\n')
            frames_sequence.append(last_frame_without_face)

            print(last_frame_without_face)

        if verbose:
            cv2.imshow("Signer detection via face detection", video_frame)  # display 
        
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        global_frame_counter += 1
    
    if verbose:
        video_capture.release()
        cv2.destroyAllWindows()


def step3_signer_detection_B_stage(verbose, minimum_duration=25, fps=25): 
    # Description: in this function it is filtered out all the periods of no-face detection with a duration less than 'minimum_duration' (default, 25).
    
    # get the root name    
    root_name = os.getcwd().split('/')[-1]

    # get the frame sequence without face
    frames_without_face = np.loadtxt(root_name + '_frames_sequence_without_signer_A-stage.txt')

        # initialization
    last_frame_without_face = 0
    period_frame_counter = 0   

    period_endings, period_durations = [], []

    for n in range(1,len(frames_without_face)):
        last_frame_without_face = frames_without_face[n-1]
        if n < len(frames_without_face)-1:
            if frames_without_face[n] == last_frame_without_face + 1:
                period_frame_counter += 1
            else:
                if verbose == True:
                    print('period_duration: ', period_frame_counter)

                if period_frame_counter >= minimum_duration:
                    period_endings.append(int(frames_without_face[n-1]))
                    period_durations.append(period_frame_counter)

                period_frame_counter = 0
        else:
            if verbose == True:
                print('period_duration: ', period_frame_counter)
            
            if period_frame_counter >= minimum_duration:
                period_endings.append(int(frames_without_face[n-1]))
                period_durations.append(period_frame_counter)

    period_beginings = list(np.array(period_endings) - np.array(period_durations))

    print('\n PERIODS WITHOUT SIGNER:')
    print('period_beginings (frame index): ', period_beginings)
    print('period_endings (frame index): ', period_endings)

    # video periods with no signer: 
    # convertion from frame_indexes to time in format hh:mm:ss,ms
    instant_beginings, instant_endings = np.array(period_beginings)/float(fps), np.array(period_endings)/float(fps)

    print('instant_beginings (seconds): ', list(instant_beginings))
    print('instant_endings (seconds): ', list(instant_endings))

    subs = []
    n=0
    for i in range(len(instant_beginings)):
        n+=1
        subs.append(srt.Subtitle(index=n, start=datetime.timedelta(seconds=instant_beginings[i]), end=datetime.timedelta(seconds=instant_endings[i]), content='no signer - period '+str(n), proprietary=''))
    
    # print(subs)
    f = open(root_name + '_frames_sequence_without_signer_B-stage.srt', 'w')
    f.writelines(srt.compose(subs))
    f.close()

    # video periods WITH signer:
    period_beginings_2, period_endings_2 = np.array(period_endings[:-1])+1, np.array(period_beginings[1:])-1
    instant_beginings_2, instant_endings_2 = period_beginings_2/float(fps), period_endings_2/float(fps)
    
    subs = []
    n=0
    for i in range(len(instant_endings)-1):
        n+=1
        subs.append(srt.Subtitle(index=n, start=datetime.timedelta(seconds=instant_beginings_2[i]), end=datetime.timedelta(seconds=instant_endings_2[i]), content='signer - period '+str(n), proprietary=''))

    # print(subs)
    f = open(root_name + '_frames_sequence_WITH_signer_B-stage.srt', 'w')
    f.writelines(srt.compose(subs))
    f.close()

    print('\n PERIODS WITH SIGNER:')
    print('period_beginings (frame index): ', list(period_beginings_2))
    print('period_endings (frame index): ', list(period_endings_2))
    
    # video periods with no signer: 
    # convertion from frame_indexes to time in format hh:mm:ss,ms
    
    print('instant_beginings (seconds): ', list(instant_beginings_2))
    print('instant_endings (seconds): ', list(instant_endings_2))
    


