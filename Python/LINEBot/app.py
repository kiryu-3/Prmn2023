import os
from pathlib import Path
import uuid

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage
import dotenv
from pyngrok import ngrok

app = Flask(__name__)
# LineBotApiオブジェクトを作成
dotenv.load_dotenv("content/info/.env")
line_bot_api = LineBotApi(os.getenv('CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('CHANNEL_SECRET'))
NGROK_DOMAIN = os.environ.get("NGROK_DOMAIN", "aaaa-bbbb-cccc.ngrok-free.app")

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)  # リクエストの署名検証を行い、正しければハンドラを実行
    except InvalidSignatureError:
        abort(400)  # 署名が無効な場合はエラーを返す
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    reply_text = event.message.text  # 受信したテキストメッセージを取得
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_text)  # 受信したテキストメッセージをそのまま返信
    )
    print("返信完了!!\ntext:", event.message.text)  # 返信が完了したことを表示

ngrok.connect(5003, hostname=NGROK_DOMAIN)

if __name__ == "__main__":
    app.run()  # アプリケーションを実行
