def flex(imgSrc,title,link,ended,btn):
    return {
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": imgSrc,
          "flex": 10,
          "align": "center",
          "size": "full",
          "aspectRatio": "3:4",
          "aspectMode": "cover",
          "action": {
            "type": "uri",
            "label": "Action",
            "uri": link
          }
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "spacing": "md",
          "action": {
            "type": "uri",
            "label": "Action",
            "uri": link
          },
          "contents": [
            {
              "type": "text",
              "text": title,
              "flex": 6,
              "size": "xl",
              "weight": "bold",
              "color": "#17160D",
              "wrap": True
            },
            {
              "type": "box",
              "layout": "vertical",
              "spacing": "sm",
              "contents": [
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "text",
                      "text": ended,
                      "flex": 0,
                      "margin": "sm",
                      "weight": "bold",
                      "color": "#DE3D3D"
                    }
                  ]
                }
              ]
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "spacer",
              "size": "xxl"
            },
            {
              "type": "button",
              "action": {
                "type": "uri",
                "label": "ดูเรื่องนี้",
                "uri": link
              },
              "color": btn,
              "height": "md",
              "style": "primary",
              "gravity": "top"
            }
          ]
        }
      }
