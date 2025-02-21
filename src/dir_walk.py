import os
from sys import path
from log.log import log_instance
from constants import FORMATS
from extract_info import MediaInfo

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
            if extension in FORMATS:
                paths.append(os.path.join(path, file))
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

def fit_subs(media_name, sub):
    media_name = media_name.split(".")
    sub = sub.split(".")
    if not media_name[0] == sub[0]:
        os.rename(sub, media_name[0]+".srt")
        log_instance.info(f"Renamed {sub} to {media_name[0]+'.srt'}")

if __name__=="__main__":
    print(get_paths_off_media("smb://100.70.137.122/myfiles/"))



