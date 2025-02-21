import os
from constants import FORMATS

def walk_dir(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            yield file
    

def crate_folder(path): 
    if not os.path.exists(path):        
        os.makedirs(path)


def get_paths_off_media(path):
    paths = []
    for file in walk_dir(path):
        file=os.path.splitext(file)
        try:
            if file[1] in FORMATS:
                paths.append(file)
        except IndexError:
            pass
    return paths         

def find_subs(path):
    list_of_subs = []
    for file in os.listdir(path):
        if file.endswith(".srt"):
            list_of_subs.append(file)
    return list_of_subs

def fit_subs(media_name, sub):
    media_name = media_name.split(".")
    sub = sub.split(".")
    if not media_name[0] == sub[0]:
        os.rename(sub, media_name[0]+".srt")

if __name__=="__main__":
    print(get_paths_off_media("smb://100.70.137.122/myfiles/"))



