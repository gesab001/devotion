import json
import os

files = os.listdir("sermons")
#print(files)
mp4s = []
for f in files:
    if f.endswith("mp4"):
        mp4s.append(f)
mp4s.sort()


vtts = []
for f in files:
    if f.endswith("vtt"):
        vtts.append(f)
vtts.sort()

#print(jsondata)
#jsondata = [{"book": "Psalms", "chapter": 91}, {"book": "Psalms", "chapter": 27 }, {"book": "Psalms", "chapter": 51}, {"book": "Psalms", "chapter": 23}, {"book": "Matthew", "chapter": 5}, {"book": "1 Corinthians", "chapter": 13}, {"book": "Hebrews", "chapter": 11}, {"book": "Revelation", "chapter": 1}]

for x in range(0, len(mp4s)):
    title = mp4s[x]
    videoSrc = title
    vttSrc = title.replace("mp4", "vtt")
    poster = title.replace("mp4", "png")
    folder = "sermons"

    link = "http://localhost:8000/player.html?video="+videoSrc+"&vtt="+vttSrc+"&folder="+folder
    html_link =  '<div class="column"'+ 'style="aspect-ratio: 16 / 9; '+ "background-image: url('"+folder+"/"+poster+"'"+'); background-size: cover;"><button onclick="window.open'+"('"+link
    html_title = html_link + "', 'videoWindow', 'width=800,height=450,noopener,noreferrer')"+'; return false;"'+">"+title+"</button></div>"
    print(html_title)

