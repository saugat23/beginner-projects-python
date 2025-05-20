import tkinter as tk
from tkinter import filedialog

from pytube import YouTube


def download_video(url, path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=path)
        print("Video downloaded successfully!")
    except Exception as e:
        print(e)

def main():
    print("Hello from youtube-downloader!")
    download_video("https://www.youtube.com/watch?v=ydOZ5YAv8Hk", "~/Desktop/") #add the youtube video url and download file path here 


if __name__ == "__main__":
    main()
