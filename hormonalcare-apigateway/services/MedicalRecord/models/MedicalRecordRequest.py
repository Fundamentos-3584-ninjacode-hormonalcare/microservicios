from pydantic import BaseModel
from typing import Optional, Dict, Any


class MedicalRecordRequest(BaseModel):
    patient_id: str
    doctor_id: str
    diagnosis: str
    treatment: str
    notes: Optional[str] = None
    attachments: Optional[Dict[str, Any]] = None
