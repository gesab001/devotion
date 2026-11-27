import subprocess
import os


filesInDir = os.listdir()
mp4s = []

for file in filesInDir:
    if file.endswith("mp4"):
        mp4s.append(file)


for mp4 in mp4s:
    video = mp4
    srt = video.replace("mp4", "srt")
    png = video.replace("mp4", "png")
    f = open(srt, "r")
    string = f.readlines()
    timestamps = []
    print(string)
    for s in string:
        if "-->" in s:
            timestamps.append(s)
    print(timestamps)    
    lastSub = timestamps[-1]
    print(lastSub)
    timestampStart = lastSub.split("-->")[0].replace(",", ".").strip()
    print(timestampStart)    
    command = 'ffmpeg -ss '+timestampStart+' -copyts -i '+video+' -vf "subtitles='+srt+'" -frames:v 1 ' + png
    subprocess.call(command, shell=True)