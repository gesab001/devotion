import subprocess
import os



files = os.listdir()
print(files)
for mp4file in files:
	if mp4file.endswith(".mp4") or mp4file.endswith(".mkv"):
		command = ' whisper "' + mp4file + '" --model medium --language en --output_format srt'
		subprocess.call(command, shell=True)