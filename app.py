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
line_bot_api = LineBotApi('rfScBFZseIDnZN6lxa7+V4QtEKRBJVM2xl8HdkrXmSarCkq7RCUcgL3kFmLdrqUE8vBsVijiuBsRU0v95aBqHNYeaC334mv2en1j++k0wmNk1M65CvdaKZOodtVehNYcfk5dl7GbRTio0KjQacSqUAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('23e167e4c67bf8f9a4fc69c2c79e47e4')


# 監聽所有來自 /callback 的 Post Request
# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['x-line-signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 學你說話
@handler.add(MessageEvent, message=TextMessage)
def echo(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
    )




if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)