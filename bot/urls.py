from django.conf.urls import url
from . import views

urlpatterns = [
    # ここのpathで/bot/hogeのhoge部分を作る
    url(r'^$', views.index, name="index"),
    url(r'^callback', views.callback), # 正規表現で/$とした場合は/で終わらなければエラーがくる
]