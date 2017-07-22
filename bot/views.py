from django.shortcuts import render
from django.http import HttpResponse
import json, requests, random
# Create your views here.


REPLY_ENDPORT = "https://api.line.me/v2/bot/message/reply" #api_reference参考
ACCESS_TOKEN = "eLDX1DFCu3LxW6KpNXxKQXnmuc5bQoj6nSpoUFUZYXkhdqc0UU5VfnTwMh8WAKYprlMqiYMWk/ijMaEBem3bAAJ3dzPvhTZoccD+XcSstklU47hCINgyvHrfTQ0PHP8SWl5RvBCkeKJ2XYv0opWOoQdB04t89/1O/w1cDnyilFU="

HEADER = {
    "Content-Type": "application/json",
    "Authorization": "Bearer" + ACCESS_TOKEN
}


def index(request):
    return HttpResponse("This is bot api")


# この引数のtextは何を表しているのか
def reply_text(reply_token, text):
    face = ["( ๑❛ᴗ❛๑)۶♡٩(๑❛ᴗ❛๑ )", "(o´艸`)ﾑﾌﾌ", "ｱﾘｶﾞﾀﾋﾞｰﾑ!!(ﾉ･_･)‥‥…━━━━━☆ﾋﾟｰｰ", "ヾ(｡>﹏<｡)ﾉ", "_(:З｣ ∠)_"]
    random_num = random.randint(0, 4)
    reply = face[random_num]
    payload = {
        "replyToken": reply_token,
        "messages": [
            {
                "type": "text",
                "text": reply
            }
        ]
    }

    requests.post(REPLY_ENDPORT, headers=HEADER, data=json.dumps(payload)) #LINEにdataをPOST

    return reply


def callback(request):
    reply = ""
    requests_json = json.loads(request.body.decode('utf-8'))# 辞書型に変更
    for req in requests_json['events']:# event内のものを回す
        reply_token = req['replyToken']# 返信先Token
        message_type = req['message']['type']# messageのtype

        if message_type == 'text':
            text = req['message']['text'] #受信メッセを取得
            reply += reply_text(reply_token, text)

    return HttpResponse(reply)