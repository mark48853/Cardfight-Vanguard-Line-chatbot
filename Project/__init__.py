import requests
from flask import Flask, request, abort
from bs4 import BeautifulSoup
import json
from Project.Config import *

app = Flask(__name__)


@app.route('/youtube', methods = ['POST','GET'])
def youtube():
    if request.method == 'POST':
        payload = request.json


        Reply_token = payload['events'][0]['replyToken']
        message = payload['events'][0]['message']['text']
        
        shouldYt = message[0:7]
        print(shouldYt)
        searchWord = message[8:len(message)]
        print(searchWord)
        if "youtube" in shouldYt :
            url = "https://www.youtube.com/results?search_query=" + searchWord
            data = requests.get(url)
        soup = BeautifulSoup(data.text,'html.parser')
        box = soup.find_all("img",{"width":"246"})
        box02 = soup.find_all("a",{"class":"yt-uix-tile-link"})
        box03 = soup.find_all("h3")
        imgUrl = []
        clipUrl = []
        i=0
        for image in box:

              print("za imagi izz:   "+image['src'])
              imgUrl.append(image['src'])
        title = []
        for a in box02:
            print("the url is :     "+a['href'])
            clipUrl.append(a['href'])
            print("theee tiiitleeee isss"+a['title'])
            title.append(a['title'])
            break
        i=0



        REPLYMSG = "soup"
        ReplyMessage(Reply_token, REPLYMSG, Channel_access_token, searchWord, imgUrl, clipUrl, title)
        return request.json, 200

    elif request.method == 'GET' :
        return 'this is method GET!!!' , 200

    else:
        abort(400)






def ReplyMessage(Reply_token, message, Line_Access_Token, sw, imgUrl, clipUrl, title):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    Authorization = 'Bearer {}'.format('ng0hDFDnoKgBkrKjG+hbQ0UiOLTkrARJiwXypO7PeX3RkLuF3KLg20ShAyCxKAxlYQdrpjRQxU0TZA/0Fo8ohwFdgnjjRvGaCq6XyxHGQ/hZ5ipGqACEnAFO1x476zuKZQHSsYQ/VANDwb/oP0os7wdB04t89/1O/w1cDnyilFU=')
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }
    data = {
        "replyToken":Reply_token,
        "messages":[{
  "type": "flex",
  "altText": title[0][0:20],
  "contents": {
    "type": "bubble",
    "header": {
      "type": "box",
      "layout": "vertical",
      "flex": 0,
      "contents": [
        {
          "type": "text",
          "text": title[0],
          "size": "xxl",
          "color": "#E82525",
          "wrap": True
        }
      ]
    },
    "hero": {
      "type": "image",
      "url": imgUrl[0],
      "size": "full",
      "aspectRatio": "20:13",
      "aspectMode": "cover",
      "action": {
        "type": "uri",
        "label": "Action",
        "uri": "https://www.youtube.com"+clipUrl[0]
      }
    },
    "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "spacer",
          "size": "lg"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "WATCH",
            "uri": "https://www.youtube.com"+clipUrl[0]
          },
          "color": "#E82525",
          "style": "primary"
        }
      ]
    }
  }
}]
    }
   



    data = json.dumps(data) ## dump dict >> Json Object
    requests.post(LINE_API, headers=headers, data=data) 
    return 200
