import json

f = open("hymnsmemorise.json", "r")
jsondata = json.loads(f.read())["items"]
#print(jsondata)
#jsondata = [{"book": "Psalms", "chapter": 91}, {"book": "Psalms", "chapter": 27 }, {"book": "Psalms", "chapter": 51}, {"book": "Psalms", "chapter": 23}, {"book": "Matthew", "chapter": 5}, {"book": "1 Corinthians", "chapter": 13}, {"book": "Hebrews", "chapter": 11}, {"book": "Revelation", "chapter": 1}]

for x in range(0, len(jsondata)):
    item = jsondata[x]
    title = item[0].title()
    link = item[1]
    html_link =  '<div class="column"><button onclick="window.open'+"('"+link
    html_title = html_link + "', 'popupWindow', 'width=500,height=400')"+'; return false;"'+">"+title+"</button></div>"
    print(html_title)

