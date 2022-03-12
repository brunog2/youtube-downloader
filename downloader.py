import pytube
from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp
import re

def dlVideo(folder, url):
    print("o folder:", folder)
    video = YouTube(url)
    title = formatTitle(video.title)
    video.streams.filter(only_audio=True).first().download("C:/Users/Efrain/Music/Catedral")
  
def formatTitle(name):
    chars = ["|", "'\'", "/", "<", ">", ":", "*", "?", '"', "'", '.', "-"]
    for ch in chars:
        if ch in name:
            name = name.replace(ch, "")
    return name

source = open("playlists.txt", "r")
playlists = []
for line in source:
    playlists.append(str(line))

x = 1
for pUrl in playlists:
    if "playlist" not in pUrl:
        video = YouTube(pUrl)
        print("Video:", video.title)
        folder = formatTitle(video.title)
        dlVideo(folder, pUrl)
        continue

    playlist = Playlist(pUrl)
    z = 1
    for url in playlist:
        print(x, z, url)
        folder = formatTitle(playlist.title)
        print("Playlist:", folder)

        dlVideo(folder, url)
        z += 1
    x += 1
