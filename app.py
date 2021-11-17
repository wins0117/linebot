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
line_bot_api = LineBotApi('+CFSbCUaF870PMDFYRbzM6Bi8fisS4TsF03mKtP7/mbrvTUze/ySZYkvZNGhAWew8vBsVijiuBsRU0v95aBqHNYeaC334mv2en1j++k0wmOKk7k/ff+mx56n6q75LAxydIwSSiq/1dV+vnBaTAfE/AdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('23e167e4c67bf8f9a4fc69c2c79e47e4')

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
def echo(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
    )




if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)