import subprocess
import os

files = os.listdir()
count = 0


for x in range(0,len(files)):
    if files[x].endswith("mp4"):
        musicFilename = files[x]
        inputFilenameMusic = musicFilename

        outputFilenameMusic = musicFilename.replace("mp4", "mp3")
        command_convert_video_to_mp3 = "ffmpeg -i " + inputFilenameMusic +  " -vn -c:a libmp3lame -q:a 2 " + outputFilenameMusic
        print(command_convert_video_to_mp3)
        subprocess.call(command_convert_video_to_mp3, shell=True)        

            
            