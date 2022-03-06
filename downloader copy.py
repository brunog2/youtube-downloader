from concurrent.futures import process
import pytube
from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp
import re
import time
from threading import Thread
from queue import Queue


def dl(url, folder, x, z):
    print("PLaylist {} / Video {}".format(x, z))
    try:
        video = YouTube(url)
        video.streams.filter(only_audio=True).first().download("C:/Users/Bruno/Music/1/{}".format(folder))
    except (Exception):
        print('\n{} indisponível!'.format(url))
        print('Continuando o processo, aguarde...\n')
        return

source = open("playlists.txt", "r")

playlists = []
for pUrl in source:
    playlist = Playlist(pUrl)
    pName = playlist.title
    videos = []

    for url in playlist:
        videos.append(url)

    chars = ["|", "'\'", "/", "<", ">", ":", "*", "?", '"', "'"]
    for ch in chars:
        if ch in pName:
            pName = pName.replace(ch, "")

    playlists.append({pName: videos})

q = Queue()
num_threads = 10

#for playlist in playlists:    
#    for i in range(num_threads):
#        worker = Thread(target=dl, args=(q,))
#        worker.setDaemon(True)
#        worker.start()

for playlist in playlists:
    folderName = playlist.getKey()
    folder = "C:/Users/bruno/Videos/Music/1/{}".format(folderName)
    print("Convertendo", folder)
    for file in os.listdir(folder):
        type = "mp4"
        if re.search(type, file):
            gpp_path = os.path.join(folder, file)
            mp3_path = os.path.join(folder, os.path.splitext(file)[0]+'.mp3')
            new_file = mp.AudioFileClip(gpp_path)
            new_file.write_audiofile(mp3_path)
            os.remove(gpp_path)
