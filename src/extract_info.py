# Description: Extracts media information from a file
from re import I
import regex as re
from constants import FORMATS

class MediaInfo:
    def __init__(self, path):
        self.path = path
        info= self._extract_info(path)
        self.name = None if info['name'] is None else info['name']
        self.season = None if info['season'] is None else info['season']
        self.episode = None if info['episode'] is None else info['episode']
        self.srt_media = self._get_type()

    def _extract_info(self, pattern):
        pattern = r'(?P<name>^[^S]*)(S(?P<season>\d+))?(E(?P<episode>\d+))?'
        match = re.match(pattern, self.path)
        return match.groupdict()

    def _get_type(self):
        extension=self.path.split(".")[-1]
        if extension in FORMATS:
            return "video"
        elif extension=="srt":
            return "subtitle"
        else:
            return "unknown"
    
    def __eq__(self, value):
        if self.srt_media == 'video' and value.srt_media == 'subtitle':
            return self.name == value.name and self.season == value.season and self.episode == value.episode
        elif self.srt_media == 'subtitle' and value.srt_media == 'video':
            return self.name == value.name and self.season == value.season and self.episode == value.episode
        else:
            return False
    
    def __str__(self):
        return f"Name: {self.name}, Season: {self.season}, Episode: {self.episode}"
    
def match_media(MediaList):
    matched=[]
    for media in MediaList:
        for value in MediaList:
            if media == value:
                if media.srt_media == "video":
                    matched.append(media, value)
                else:
                    matched.append(value, media)
    return matched
#test
if __name__ == "__main__":
    path = "House_MD_S01E01.mkv"
    media = MediaInfo(path)
    print(media)