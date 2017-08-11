from django.shortcuts import render
from django.http import HttpResponse
from gensim.models import word2vec
import json, requests, os

# Create your views here.


REPLY_ENDPORT = "https://api.line.me/v2/bot/message/reply" #api_reference参考
ACCESS_TOKEN = "your access_token"

# Bearerのあとインデントをつけること!
HEADER = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + ACCESS_TOKEN
}

#これで相対パスを取得
model_path = os.path.dirname(__file__) + "/model_person/souseki.model"
model_data = word2vec.Word2Vec.load(model_path)


def index(request):
    return HttpResponse("This is bot api")


def reply_text(reply_token, text):
    try:
        reply_data = model_data.most_similar(positive=[text])
        txt = reply_data[0][0]
        vector = float(reply_data[0][1])
        if vector >= 0.8:
            reply = "うむ！それはまさしく{0}であるな！".format(txt)
        elif vector >= 0.5:
            reply = "そうだな...それはおそらく{0}であろう".format(txt)
        else:
            reply = "うーむ...私にとっては{0}だと思うのだが...".format(txt)
    except KeyError:
        reply = "すまぬが{0}と云う言葉は聞いたことがないな...".format(text)


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
    requests_json = json.loads(request.body.decode('utf-8'))# 辞書型に変更
    for req in requests_json['events']:# event内のものを回す
        reply_token = req['replyToken']# 返信先Token
        message_type = req['message']['type']# messageのtype

        if message_type == 'text':
            text = req['message']['text'] # 受信メッセを取得
            # リストで返ってくるため
            reply = reply_text(reply_token, text)


    return HttpResponse(reply) # キチンと動いているか確かめる(postman等を使う)