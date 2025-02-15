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
srt = subtitles.download(response.data[0])
with open ("breaking_bad.srt", "wb") as f:
    f.write(srt)

def get_subs(query, season_number, episode_number, language, sub_name):
    response = subtitles.search(query=query, season_number=season_number, episode_number=episode_number, languages=language)
    response_dict = response.to_dict()
    print(response_dict)
    srt = subtitles.download(response.data[0])
    if sub_name is None:
        sub_name = query
    with open (f"{sub_name}.srt", "wb") as f:
        f.write(srt)