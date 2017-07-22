from gensim.models import word2vec
import os


model_path = os.path.dirname(__file__) + "/model_person/夏目漱石.model"
model = word2vec.Word2Vec.load(model_path)

try:
    r_data = model.most_similar(positive=[])
    print("類似度を表示します")
    print(r_data)
except Exception as e:
    print(e, "により出力できませんでした.")
try:
    t_data = model.most_similar(negative=[])
    print("類似度を表示します")
    print(t_data)
except Exception as e:
    print(e, "により出力できませんでした.")
