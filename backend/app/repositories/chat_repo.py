from sqlalchemy.orm import Session
from ..models.chat import ChatHistory  

def save_chat_message(db: Session, role: str, message: str, session_id: str = "default_session"):

    db_message = ChatHistory(
        session_id=session_id,
        role=role,
        message=message
    )
    db.add(db_message) 
    db.commit()
    db.refresh(db_message)
    
    return db_message

def get_chat_history(db: Session) -> list[ChatHistory]:

    return db.query(ChatHistory).order_by(ChatHistory.id).all()