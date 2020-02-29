def flex(cardSkill,cardImgSrc,cardName):
    return {
  "type": "flex",
  "altText": "Searching Result",
  "contents": {
    "type": "bubble",
    "hero": {
      "type": "image",
      "url": cardImgSrc,
      "size": "full",
      "aspectRatio": "3.1:4.6",
      "aspectMode": "cover",
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": cardName,
          "size": "xl",
          "weight": "bold",
          "color": "#9FBE02",
          "wrap": True
        },
        {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "margin": "lg",
          "contents": [
            {
              "type": "box",
              "layout": "baseline",
              "spacing": "sm",
              "contents": [
                {
                  "type": "text",
                  "text": cardSkill,
                  "flex": 5,
                  "size": "sm",
                  "color": "#666666",
                  "wrap": True
                }
              ]
            }
          ]
        }
      ]
    }
  }
}
            