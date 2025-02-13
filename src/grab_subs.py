import opensubtitlescom as osc
import os
from dotenv import dotenv_values

config=dotenv_values(".env")

API_KEY=config['API_KEY']

MY_USERNAME=config['MY_USERNAME']

MY_PASSWORD=config['MY_PASSWORD']


subtitles = osc.OpenSubtitles("SubGrabber v1.0.0", API_KEY)

subtitles.login(MY_USERNAME, MY_PASSWORD)
response = subtitles.search(query="breaking bad", season_number=1, episode_number=1, languages="en")
response_dict = response.to_dict()
print(response_dict)
srt = subtitles.download_and_save(response.data[0])
print(srt)