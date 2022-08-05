""" import queue

q = queue.Queue()

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get()) """

""" import threading as t
import time

def func(x):
    time.sleep(3)
    print(f'Taks {x} is done.')
    
worker1 = t.Thread(target=func, args=(1,))
worker2 = t.Thread(target=func, args=(2,))

worker1.start()
worker2.start() """

import queue
import threading as t
import time
from fileinput import filename
import pytube
from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp
import re

def dlVideo(q, thread_no):
    while True:
        print(q.get())
        url = q.get()[0]
        folder = q.get()[1]
        q.task_done()
        video = YouTube(url)
        print(f'Thread #{thread_no} attemping to download #{url} in the queue.\nBaixando: {video.title}')

        title = formatTitle(video.title)+".mp4"
        if not os.path.exists("C:/Users/Bruno/Videos/{}/{}".format(folder, title)):
            try:
                video.streams.filter(only_audio=True).first().download("C:/Users/Bruno/Videos/{}".format(folder), filename=title)
            except:
                print("Não foi possível baixar o arquivo")
        else:
            print("Arquivo já existente... Pulando")
            continue


def formatTitle(name):
    chars = ["|", "'\'", "/", "<", ">", ":", "*", "?", '"', "'", '.', "-"]
    for ch in chars:
        if ch in name:
            name = name.replace(ch, "")
    return name


source = open("C:\playlists.txt", "r")
playlists = []

for line in source:
    playlists.append(str(line))

videos = []
x = 1
for pUrl in playlists:
    if "playlist" not in pUrl:
        video = YouTube(pUrl)
        #print("Video:", video.title)
        folder = formatTitle(video.title)
        dlVideo(folder, pUrl)
        continue

    playlist = Playlist(pUrl)
    z = 1
    for url in playlist:
        folder = formatTitle(playlist.title)
        #print(f'Playlist {x}')
        #print(f'Música {z} da playlist {folder}: {url}')

        videos.append([url, folder])
        z += 1
    x += 1


q = queue.Queue()

for i in range(8):
    downloader = t.Thread(target=dlVideo, args=(q, i,), daemon=True)
    downloader.start()
print(videos)
for video in videos:
    #print(video)
    q.put(video)

q.join()
