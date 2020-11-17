import os

import cv2
import time
import shutil


def get_vid_number():
    with open('vid_number.txt', 'r') as f:
        vid_number = int(f.readline(), 16)
        f.close()
    with open('vid_number.txt', 'w') as f:
        f.write(str(hex(vid_number + 1)))
        f.close()
    return vid_number


def split_frames(image_prepend, from_path, to_path):
    # Log the time
    time_start = time.time()
    # Start capturing the feed
    cap = cv2.VideoCapture(from_path)
    # Find the number of frames
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print("Number of frames Available: ", video_length)
    count = 0
    print("Converting video..\n")
    # Start converting the video
    ret = True
    while ret:
        # Extract the frame
        ret, frame = cap.read()
        # Write the results back to output location.
        # only take every third frame
        if count % 3 == 0:
            full_image_path = to_path + r"\{}{}.jpg".format(image_prepend, str(count).zfill(5))
            print(full_image_path)
            cv2.imwrite(full_image_path, frame)
            print('frame {} completed'.format(count))
        count = count + 1
    cap.release()
    print("Done extracting frames.\n%d frames extracted" % count)


def move_to_class_folder(to_path, from_path):
    for file in os.listdir(from_path):
        shutil.move(os.path.join(from_path, file), to_path)
    count = 0
    for _ in os.listdir(to_path):
        count += 1
    print('Files found in {}\n'.format(to_path), count)


if __name__ == "__main__":
    vid_path = r'E:\imageSets\Pokemon\videos\input\a.mkv'
    dir_path = r'E:\imageSets\Pokemon\videos\test'
    place_path = r'E:\imageSets\Pokemon\dataset\data\Charizard'
    move_to_class_folder(place_path, dir_path)


    #video_number = get_vid_number()

    #split_frames(video_number, vid_path, dir_path)
