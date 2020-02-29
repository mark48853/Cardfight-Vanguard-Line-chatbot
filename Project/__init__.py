import requests
from flask import Flask, request, abort
from bs4 import BeautifulSoup
import json
from Project.flex import *
from Project.Config import *

app = Flask(__name__)


@app.route('/vg', methods = ['POST','GET'])
def vg():
    if request.method == 'POST':
        payload = request.json

        Reply_token = payload['events'][0]['replyToken']
        message = payload['events'][0]['message']['text']
        url = "https://en.cf-vanguard.com/cardlist/?cardno=" + message + "EN"
        data = requests.get(url)
        soup = BeautifulSoup(data.text,'html.parser')
        card = soup.find("div",{"class":"effect"})
        cardPic = soup.find("div",{"class":"main"})
        print("___________________________________")
        cardSkill = card.text
        cardImgSrc = ""
        cardName = ""
        print(card)
        for img in cardPic:
          print (img['src'])
          cardImgSrc = img['src']
          cardName = img['alt']


        
        ReplyMessageSearch (Reply_token, message, Channel_access_token, cardSkill, cardImgSrc, cardName)

        return request.json, 200

    elif request.method == 'GET' :
        return 'this is method GET!!!' , 200

    else:
        abort(400)






def ReplyMessageSearch(Reply_token, message, Line_Access_Token, cardSkill, cardImgSrc, cardName):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    Authorization = 'Bearer {}'.format(Channel_access_token)
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }
    data = {
        "replyToken":Reply_token,
        "messages":[
          flex(cardSkill,cardImgSrc,cardName)
  ]
}
    
                    

    data = json.dumps(data) ## dump dict >> Json Object
    requests.post(LINE_API, headers=headers, data=data) 
    return 200