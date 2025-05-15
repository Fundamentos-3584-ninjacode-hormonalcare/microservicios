from pydantic import BaseModel, Field, EmailStr
from datetime import datetime

class ProjectRequestResource(BaseModel):
    name: str = Field(..., min_length=1)
    surname: str = Field(..., min_length=1)
    email: EmailStr
    phone: str = Field(..., min_length=1)
    address: str = Field(..., min_length=1)
    city: str = Field(..., min_length=1)
    summary: str = Field(..., min_length=1)
    businessId: int = Field(..., gt=0)
    contractorId: int = Field(..., gt=0)
    deadlineDate: datetime
    rooms: int = Field(..., gt=0)
    budget: int = Field(..., gt=0)

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }