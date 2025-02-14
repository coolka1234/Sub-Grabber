import os

def walk_dir(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            yield os.path.join(root, file)
    
for file in walk_dir("."):
    print(file)

def crate_folder(path):
    if not os.path.exists(path):        
        os.makedirs(path)

crate_folder("subs")