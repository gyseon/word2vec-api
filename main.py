from fastapi import FastAPI
from model_loader import load_model

app = FastAPI()
model = load_model()

@app.get("/similarity/")
def get_similarity(word: str):
    try:
        similar_words = model.most_similar(word, topn=10)
        return {"word": word, "similar_words": [w[0] for w in similar_words]}
    except KeyError:
        return {"error": "단어를 찾을 수 없음"}
