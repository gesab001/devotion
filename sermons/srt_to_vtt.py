import re

def convert_srt_to_vtt(srt_path: str, vtt_path: str) -> None:
    with open(srt_path, 'r', encoding='utf-8') as srt_file:
        content = srt_file.read()

    # Replace commas with periods in timestamps (e.g., 00:01:23,456 -> 00:01:23.456)
    vtt_content = re.sub(r'(\d{2}:\d{2}:\d{2}),(\d{3})', r'\1.\2', content)

    with open(vtt_path, 'w', encoding='utf-8') as vtt_file:
        vtt_file.write("WEBVTT\n\n" + vtt_content.strip() + "\n")

import os

srts = os.listdir()

for f in srts:
  if f.endswith("srt"):
      output = f.replace("srt", "vtt")
      convert_srt_to_vtt(f, output)