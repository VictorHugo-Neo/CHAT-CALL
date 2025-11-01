from fastapi import APIRouter
from .schemas import ChatRequest, ChatResponse
from .services import chat_service

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def handle_chat_request(request: ChatRequest):

    resposta_da_ia = chat_service.get_ai_response(request.pergunta)
    return ChatResponse(resposta=resposta_da_ia)