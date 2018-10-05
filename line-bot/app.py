# app for line-bot
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('LstsRPE6Ot/Mat3+ue4xI132lcvC3nQJh+TKbcR9pm2qF7NMS4Z5UHV4cuLoth9pC5HXziIjea5BHDF00JkwWiKfSXU5U/8o3XiAeGnjhJMP3Ph6WcD2n7zUunD19Y3iNe2HcZueoLwhjKX4O0gN0AdB04t89/1O/w1cDnyilFU=')

handler = WebhookHandler('b5e01cf2cce2dddde6a36ba30e6934d1')

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


    @handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
    
