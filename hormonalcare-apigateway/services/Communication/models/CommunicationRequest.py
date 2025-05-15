from pydantic import BaseModel
from typing import Optional, List, Dict, Any


class CommunicationRequest(BaseModel):
    sender_id: str
    recipient_id: str
    message: str
    message_type: str  # "text", "image", "video", etc.
    attachments: Optional[List[Dict[str, Any]]] = None
