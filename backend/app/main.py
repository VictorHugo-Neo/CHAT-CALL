from fastapi import FastAPI
from .routes import router  
from fastapi.middleware.cors import CORSMiddleware 
app = FastAPI(
    title="Chat API",
    description="Backend para o Chat-Call com IA",
    version="0.1.0"
)
origins = [
    "http://localhost",
    "http://localhost:3000", 
    "http://localhost:5173", 
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def read_root():
    return {"status": "Chat API está online!"}

app.include_router(router, prefix="/api/v1", tags=["chat"])
