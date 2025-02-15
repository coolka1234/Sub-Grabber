import os
from consts import FORMATS

def walk_dir(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            yield file
    
for file in walk_dir("."):
    print(file)

def crate_folder(path): 
    if not os.path.exists(path):        
        os.makedirs(path)

def get_paths_off_media(path):
    paths = []
    for file in walk_dir(path):
        if file.endswith(FORMATS):
            paths.append(file)
    return paths        

crate_folder("subs")