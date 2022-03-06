import pytube
from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp
import re

print(pytube.__version__)

source = open("playlists.txt", "r")
playlists = []
for line in source:
    playlists.append(str(line))

x = 1
for pUrl in playlists:
    playlist = Playlist(pUrl)
    print("Playlist:", playlist.title)
    z = 1
    for url in playlist:
        print(x, z, url)
        try:
            video = YouTube(url)
            folder = playlist.title
            chars = ["|", "'\'", "/", "<", ">", ":", "*", "?", '"', "'"]
            for ch in chars:
                if ch in folder:
                    folder = folder.replace(ch, "")
            video.streams.filter(only_audio=True).first().download("C:/Users/bruno/Music/{}".format(folder))
        except (Exception):
            print ('Existe algum vídeo indisponível, o mesmo não pôde ser baixado! \n')
            print ('Continuando o processo, aguarde...\n')
            pass
            
        z += 1
    x += 1


for y in range(1, x):
    folder = "C:/Users/bruno/Videos/Downloads/{}".format(y)
    for file in os.listdir(folder):
        type = "mp4"
        if re.search(type, file):
            gpp_path = os.path.join(folder,file)
            mp3_path = os.path.join(folder,os.path.splitext(file)[0]+'.mp3')
            new_file = mp.AudioFileClip(gpp_path)
            new_file.write_audiofile(mp3_path)
            os.remove(gpp_path)

