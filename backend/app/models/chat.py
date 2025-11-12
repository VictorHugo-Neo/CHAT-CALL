from sqlalchemy import Column, Integer, String, DateTime, func
from ..core.database import Base 

class ChatHistory(Base):
    
    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, index=True, default="default_session")  
    role = Column(String, nullable=False) 
    message = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())