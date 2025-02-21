import os
from sys import path
from extract_info import MediaInfo, match_media
from log.log import log_instance
from constants import FORMATS
import shutil

def walk_dir(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            yield file
    

def crate_folder(path): 
    if not os.path.exists(path):        
        os.makedirs(path)


def get_paths_off_media(path):
    log_instance.info(f"Looking for MEDIA files in {path}")
    paths = []
    for file in walk_dir(path):
        log_instance.info(f"Found MEDIA file: {file}")
        try:
            extension=os.path.splitext(file)[1][1:]
            if extension in FORMATS or extension=="srt":
                paths.append(MediaInfo(os.path.join(path, file)))
        except IndexError:
            pass
    return paths         

def find_subs(file_path):
    list_of_subs = []
    path=os.path.dirname(file_path)
    log_instance.info(f"Looking for SUB files in {path}")
    for file in os.listdir(path):
        log_instance.info(f"Found SUB file: {file}")
        if file.endswith(".srt"):
            list_of_subs.append(file)
    return list_of_subs


def fit_subs(MediaList):
    matched_media=match_media(MediaList)
    for media in matched_media:
        if len(media)==2:
            if media[0].path!=media[1].path:
                try:
                    shutil.copy(media[1].path, media[0].path.replace(media[0].path.split(".")[-1], "srt"))
                except shutil.SameFileError:
                    pass
                log_instance.info(f"Subtitles for {media[0].path} matched and renamed")
            else:
                log_instance.info(f"Subtitles for {media[0].path} matched")
        else:
            log_instance.info(f"Subtitles for {media[0].path} not found")
    return matched_media

if __name__=="__main__":
    print(get_paths_off_media("smb://100.70.137.122/myfiles/"))



