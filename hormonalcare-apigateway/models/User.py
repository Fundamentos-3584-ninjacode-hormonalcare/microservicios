from pydantic import BaseModel, EmailStr
from typing import Optional


class User(BaseModel):
    id: Optional[str] = None
    email: EmailStr
    role: str  # patient, doctor, admin
    firstName: str
    lastName: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    class Config:
        from_attributes = True
