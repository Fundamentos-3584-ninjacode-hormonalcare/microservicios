from pydantic import BaseModel
from typing import Optional, List, Dict, Any


class MedicalRecord(BaseModel):
    id: Optional[str] = None
    patient_id: str
    doctor_id: str
    diagnosis: str
    treatment: str
    notes: Optional[str] = None
    attachments: Optional[Dict[str, Any]] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    class Config:
        from_attributes = True
