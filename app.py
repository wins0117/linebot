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
line_bot_api = LineBotApi('k9LZWs5heFSz8h8EtdKt7ouN/i+3iXAv5b9jy/qkyiUhSJy1E+1et+2gGJPK8MEC8vBsVijiuBsRU0v95aBqHNYeaC334mv2en1j++k0wmNsSrNptFJrnYDBnPReITLU3InrJWb0RzJNh9w/NukdfAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('5ff724a21c5de4e1bbe7f8d62ba50e9e')


# 監聽所有來自 /callback 的 Post Request
# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

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