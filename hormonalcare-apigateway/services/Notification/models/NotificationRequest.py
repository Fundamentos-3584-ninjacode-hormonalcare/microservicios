from pydantic import BaseModel
from typing import Optional


class NotificationRequest(BaseModel):
    recipient_id: str
    sender_id: Optional[str] = None
    title: str
    message: str
    type: str  # e.g. "appointment", "reminder", "message"
