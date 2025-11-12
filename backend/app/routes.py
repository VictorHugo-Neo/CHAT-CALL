from fastapi import APIRouter, Depends  
from sqlalchemy.orm import Session      
from .schemas import ChatRequest, ChatResponse
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