import os
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)
# Channel Access Token
line_bot_api = LineBotApi('+qRQRA2D5y45IzqBaxQwSwHNC/UhOAF8VaCPHB6jyFmbGaB4L7R+lhGDK20OJxcWZHTswmciwbucdXx2IycoTcsjvMktiWooZe/hTzJHW+/NAkDlYlX4u25ZI17R6r9yK/lnVQLMIxDiAGNvch4BeQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('0d6d26b3d08db94b95f9ae1b2f40cb43')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息 

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text.lower()

    if msg == 'hi':
        message = TemplateSendMessage(
        template=ButtonsTemplate(
        thumbnail_image_url='https://i0.wp.com/www.womstation.com/wp-content/uploads/2018/11/%E9%9F%93%E5%9C%8B4.png?w=1280&ssl=1',
        title='第一個小功能',
        text='測試雞肋功能',
        actions=[
            URITemplateAction(
                label='熱門youtube',
                uri='https://www.youtube.com/feed/trending'
            ),
            URITemplateAction(
                label='小新聞',
                uri='https://news.google.com/?hl=zh-TW&tab=wn1&gl=TW&ceid=TW:zh-Hant'
            ),
            URITemplateAction(
                label='IGIG',
                uri='https://www.instagram.com/?hl=zh-tw'
            ),

            ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    else:
    	message = TextSendMessage(text= msg)
    	line_bot_api.reply_message(event.reply_token, message)




if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)