import json

f = open("memoryverse_json.json", "r")
jsondata = json.loads(f.read())["items"]
#jsondata = [{"book": "Psalms", "chapter": 91}, {"book": "Psalms", "chapter": 27 }, {"book": "Psalms", "chapter": 51}, {"book": "Psalms", "chapter": 23}, {"book": "Matthew", "chapter": 5}, {"book": "1 Corinthians", "chapter": 13}, {"book": "Hebrews", "chapter": 11}, {"book": "Revelation", "chapter": 1}]

for x in range(0, len(jsondata)):
    item = jsondata[x]
    book = item["book"] #"Psalms"
    chapter = str(item["chapter"])
    start = ""
    end = ""
    title = ""
    if "start" in item:
        start = str(item["start"])
        end = str(item["end"])
    if "title" in item:
        title = item["title"]
        
    html_book_chapter =  '<div class="column"><button onclick="window.open'+"('memoryverse.html?book="+book+"&chapter="+chapter
    html_start = html_book_chapter+'&start='+start
    html_end = html_start + '&end='+end
    html_title =  ""
    if title=="":
        html_title = html_end + "', 'popupWindow', 'width=500,height=400')"+'; return false;"'+">"+book + " " + chapter+"</button></div>"
    else:
        html_title = html_end + "', 'popupWindow', 'width=500,height=400')"+'; return false;"'+">"+title+"</button></div>"
    print(html_title)

