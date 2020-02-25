import requests
from flask import Flask, request, abort
from bs4 import BeautifulSoup
import json
from Project.flex import *
from Project.Config import *

app = Flask(__name__)


@app.route('/anime', methods = ['POST','GET'])
def anime():
    if request.method == 'POST':
        payload = request.json

        Reply_token = payload['events'][0]['replyToken']
        message = payload['events'][0]['message']['text']
        searchOrNot = message[0:6].lower()
        print(searchOrNot)
        if "search" in searchOrNot:
          searchWord = message[7:len(message)]
          print(searchWord)
          url = "https://www.anime-sugoi.com/index.php?search=" + searchWord
          data = requests.get(url)
          soup = BeautifulSoup(data.text,'html.parser')
          divv = soup.find("div",{"class":"panel-body"})
          atag = divv.find_all("a")
          spantag = divv.find_all("span",{"class":"label-danger"})
          box = divv.find_all("img",{"class":"img-thumbnail"})
          print(box)
          imageList = []
          titleList = []
          linkList = []
          endedOrNot = []
          for image in box:
            print(image['src'])
            imageList.append(image['src'])
            print(image['title'])
            titleList.append(image['title'])
          z=2
          for a in atag:
            if z % 2 == 0:
              linkList.append(a['href'])
              print(a['href'])
            z = z + 1
          for span in spantag:
            print(span.text)
            endedOrNot.append(span.text)
          ReplyMessageSearch (Reply_token, message, Channel_access_token, imageList, titleList, linkList, endedOrNot)
 



        return request.json, 200

    elif request.method == 'GET' :
        return 'this is method GET!!!' , 200

    else:
        abort(400)






def ReplyMessageSearch(Reply_token, message, Line_Access_Token, imgSrc, title, link, ended):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    Authorization = 'Bearer {}'.format('PuM0ErN/81YoFSbLiHj07P+Y+IpW5eVZOXklqyB96MJn+kOrpRgmDRH2C0xgSP1ky7DDnpJ10g2wPds29FsGC2b3tvfV+R9vf38qZOBxfXqkIMSCxT29SzhusM+bf1+vq21Va3au1f23whbFRveB+AdB04t89/1O/w1cDnyilFU=')
    print(Authorization)
    print(len(imgSrc))
    content = []
    i = 0
    for i in range(len(imgSrc)):
      content.append(flex(imgSrc[i],title[i],link[i],ended[i]))
      if i == 9:
        break
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }
    data = {
        "replyToken":Reply_token,
        "messages":[{
  "type": "flex",
  "altText": "ผลการค้นหา",
  "contents": {
    "type": "carousel",
    "contents": 
          content
        
  }
  }]
}
    
                    

    data = json.dumps(data) ## dump dict >> Json Object
    requests.post(LINE_API, headers=headers, data=data) 
    return 200