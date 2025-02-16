# Description: Extracts media information from a file
import regex as re

class MediaInfo:
    def __init__(self, path):
        self.path = path
        self.info = self._extract_info()

    def _extract_info(self):
        pattern = re.compile(r'(?P<name>.*?)(?P<ext>\..*?)$')
        match = pattern.match(self.path)
        if match:
            return match.groupdict()
        return None  