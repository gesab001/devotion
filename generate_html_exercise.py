import json
import os

folder = "workout"
files = os.listdir(folder)
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
    buttonTitle = folder.title() + " " + str(x)
    poster = title.replace("mp4", "png")
    link = "player.html?video="+videoSrc+"&vtt="+vttSrc+"&folder="+folder
    background_image_backup = "https://gesab001.github.io/videos/"+folder+"/"+poster
    aTag = '<a href="'+ link +'" target="_blank" rel="noopener noreferrer" onclick="window.open(this.href, '+"'videoWindow', 'width=800,height=450,noopener,noreferrer'); return false;"+'">'              
    html_link =  aTag + '<div class="column"'+ 'style="aspect-ratio: 16 / 9; '+ "background-image: url('"+folder+"/"+poster+"'"+'), '+ "url('"+background_image_backup+"'"+')'+'; background-size: cover;">'+"</div></a>"
    print(html_link)

