from pydantic import BaseModel
from datetime import datetime

class ChatRequest(BaseModel):
    pergunta: str

class ChatResponse(BaseModel): 
    resposta: str
    
class HistoryMessage(BaseModel):

    role: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True