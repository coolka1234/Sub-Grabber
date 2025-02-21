from gettext import find
from dir_walk import get_paths_off_media, find_subs, fit_subs
from grab_subs import get_subs

def main(path, **kwargs):
    paths=get_paths_off_media(path)
    for path in paths:
        find_subs(path)
        for sub in find_subs(path):
            fit_subs(path, sub)
        
if __name__=="__main__":
    main("/test_folder")