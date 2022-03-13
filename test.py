import os
import subprocess

direc = r"C:/Users/Bruno/Music/"
all = os.walk(direc)

for dirpath, folders, filename in all:    
    x = 1

    for folder in folders:
        folderMusic = folder
        folder = r"C:/Users/Bruno/Music/{}".format(folder)
        print(folder)
        for file in os.listdir(folder):
            initialFile = os.path.join(folder, file)
            print("Arquivo inicial:", initialFile)
            finalFile = os.path.join(folder, os.path.splitext(file)[0]+".mp3")
            print("Arquivo final:", finalFile)
            subprocess.run([
                'ffmpeg',
                '-i', initialFile,
                '-b:a', '64k',
                '-n',
                finalFile
            ])
