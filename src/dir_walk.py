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
        if file[1] in FORMATS:
            paths.append(file)
    return paths        

if __name__=="__main__":
    print(get_paths_off_media("smb://100.70.137.122/myfiles/"))



