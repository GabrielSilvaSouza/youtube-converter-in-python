from pytube import YouTube
from moviepy.editor import AudioFileClip
import os


def download_video(url, filepath):
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video.download(filepath)
    return video.default_filename

def convert_to_mp3(video_name):
    video = AudioFileClip(f'C:/Users/Gabriel/Downloads/{video_name}')
    video.write_audiofile(f'C:/Users/Gabriel/Downloads/{video_name[:-4]}.mp3')
    return video_name[:-4]


