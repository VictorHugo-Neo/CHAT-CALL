from fastapi import APIRouter, Depends  
from sqlalchemy.orm import Session      
from typing import List
from .schemas import ChatRequest, ChatResponse, HistoryMessage
from .services import chat_service
from .core.database import get_db
from .repositories import chat_repo

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def handle_chat_request(
    request: ChatRequest, 
    db: Session = Depends(get_db)  
):
    
    resposta_da_ia = chat_service.get_ai_response(request.pergunta)
    
    try:
        chat_repo.save_chat_message(
            db=db, 
            role="user", 
            message=request.pergunta
        )
        chat_repo.save_chat_message(
            db=db, 
            role="ai", 
            message=resposta_da_ia
        )
        
        print("INFO: Histórico do chat salvo no banco.")
        
    except Exception as e:
        print(f"ERRO: Falha ao salvar histórico no banco: {e}")
    return ChatResponse(resposta=resposta_da_ia)

@router.get("/chat/history", response_model=List[HistoryMessage])
def get_history(db: Session = Depends(get_db)):

    history_db = chat_repo.get_chat_history(db)
    
    history_api = [
        HistoryMessage(
            role=msg.role, 
            content=msg.message, 
            created_at=msg.created_at
        ) 
        for msg in history_db
    ]
    
    return history_api