from pydantic import BaseModel
from typing import Optional, List, Dict, Any


class Message(BaseModel):
    id: Optional[str] = None
    conversation_id: str
    sender_id: str
    recipient_id: str
    content: str
    message_status: str
    created_at: Optional[str] = None
    read_at: Optional[str] = None

    class Config:
        from_attributes = True
        
class Conversation(BaseModel):
    id: Optional[str] = None
    participants: str
    last_message_content: str
    last_message_date: str
    created_at: Optional[str] = None
    read_at: Optional[str] = None

    class Config:
        from_attributes = True
