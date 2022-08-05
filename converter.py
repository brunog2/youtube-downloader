import pytube
from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp
import re

direc = "C:/Users/Bruno/Music/"
all = os.walk(direc)

for dirpath, folders, filename in all:    
    x = 1

    for folder in folders:
        folderMusic = folder
        folder = "C:/Users/Bruno/Music/{}".format(folder)
        print(folder)
        for file in os.listdir(folder):
            type = "mp4"
            if re.search(type, file):
                try:
                    gpp_path = os.path.join(folder,file)
                    mp3_path = os.path.join(folder,os.path.splitext(file)[0]+'.mp3')
                    new_file = mp.AudioFileClip(gpp_path)
                    new_file.write_audiofile(mp3_path)
                    os.remove(gpp_path)
                except:
                    print("Nao foi possivel converter o arquivo")