from pydantic import BaseModel
from typing import Optional, List, Dict, Any


class Communication(BaseModel):
    id: Optional[str] = None
    sender_id: str
    recipient_id: str
    message: str
    message_type: str  # "text", "image", "video", etc.
    attachments: Optional[List[Dict[str, Any]]] = None
    created_at: Optional[str] = None
    read_at: Optional[str] = None

    class Config:
        from_attributes = True
