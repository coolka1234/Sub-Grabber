# Description: Extracts media information from a file
from re import I
import regex as re

class MediaInfo:
    def __init__(self, path):
        self.path = path
        info= self._extract_info(path)
        self.name = None if info['name'] is None else info['name']
        self.season = None if info['season'] is None else info['season']
        self.episode = None if info['episode'] is None else info['episode']

    def _extract_info(self, pattern):
        pattern = r'(?P<name>^[^S]*)(S(?P<season>\d+))?(E(?P<episode>\d+))?'
        match = re.match(pattern, self.path)
        return match.groupdict()

    
    def __str__(self):
        return f"Name: {self.name}, Season: {self.season}, Episode: {self.episode}"

#test
if __name__ == "__main__":
    path = "House_MD_S01E01.mkv"
    media = MediaInfo(path)
    print(media)