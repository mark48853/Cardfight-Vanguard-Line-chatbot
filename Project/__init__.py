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
        
        shouldYoutube = message[0:7]
        print(shouldYoutube)
        searchWord = message[8:len(message)]
        print(searchWord)
        if youtube or Youtube in shouldYoutube :
            url = "https://www.youtube.com/results?search_query=" + searchWord
            data = requests.get(url)
        soup = BeautifulSoup(data.text,'html.parser')
        box = soup.find_all("img")
        box02 = soup.find_all("a")
        box03 = soup.find_all("h3")
        imgUrl = []
        clipUrl = []
        i=0
        for image in box:
            
            if i >= 6 and i < 10 :
                print(image['src'])
                imgUrl.append(image['src'])
            if i == 10:
                break
            i=i+1
        i=0
        for a in box02:
            if i >=3:
                print(a['href'])
                clipUrl.append(a['href'])
                break
            i=i+1
        i=0
        title = []
        for h3 in box02:
            if i ==4:
                print(h3.text)
                title.append(h3.text)
                # break
            i=i+1


        REPLYMSG = "soup"
        ReplyMessage(Reply_token, REPLYMSG, Channel_access_token, searchWord, imgUrl, clipUrl, title, box02)
        return request.json, 200

    elif request.method == 'GET' :
        return 'this is method GET!!!' , 200

    else:
        abort(400)






def ReplyMessage(Reply_token, message, Line_Access_Token, sw, imgUrl, clipUrl, title, box02):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    Authorization = 'Bearer {}'.format('ng0hDFDnoKgBkrKjG+hbQ0UiOLTkrARJiwXypO7PeX3RkLuF3KLg20ShAyCxKAxlYQdrpjRQxU0TZA/0Fo8ohwFdgnjjRvGaCq6XyxHGQ/hZ5ipGqACEnAFO1x476zuKZQHSsYQ/VANDwb/oP0os7wdB04t89/1O/w1cDnyilFU=')
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }
    data = {
        "replyToken":Reply_token,
        "messages":[
          "type": "text",
          "text": box02
        ]
    }
   



    data = json.dumps(data) ## dump dict >> Json Object
    requests.post(LINE_API, headers=headers, data=data) 
    return 200
