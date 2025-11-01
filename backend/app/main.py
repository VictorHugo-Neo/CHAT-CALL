from fastapi import FastAPI
from .routes import router  

app = FastAPI(
    title="Chat API",
    description="Backend para o Chat-Call com IA",
    version="0.1.0"
)

@app.get("/")
def read_root():
    return {"status": "Chat API está online!"}


