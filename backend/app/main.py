from fastapi import FastAPI
from .routes import router  

app = FastAPI(
    title="Chat API",
    description="Backend para o Chat-Call com IA",
    version="0.1.0"
)
origins = [
    "http://localhost",
    "http://localhost:3000", # Porta padrão do create-react-app
    "http://localhost:5173", # Porta padrão do Vite
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

app.include_router(router, prefix="/api/v1")
