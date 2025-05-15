from pydantic import BaseModel
from typing import Optional


class Notification(BaseModel):
    id: Optional[str] = None
    recipient_id: str
    sender_id: Optional[str] = None
    title: str
    message: str
    type: str  # e.g. "appointment", "reminder", "message"
    read: bool = False
    created_at: Optional[str] = None

    class Config:
        from_attributes = True
