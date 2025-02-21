from gettext import find
from dir_walk import get_paths_off_media, find_subs, fit_subs
from grab_subs import get_subs
from log.log import log_instance

def main(path, **kwargs):
    paths=get_paths_off_media(path)
    log_instance.info(f"Returned MEDIA paths: {paths}")
    fit_subs(paths)
        
if __name__=="__main__":
    main("/home/coolka/projects/python/SubGrabber/test_folder")