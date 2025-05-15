from pydantic import BaseModel, Field
from datetime import datetime

class ProjectResource(BaseModel):
    name: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1, max_length=500)
    businessId: int = Field(..., gt=0)
    contractorId: int = Field(..., gt=0)
    startDate: datetime
    finishDate: datetime
    image: str = Field(..., min_length=1, max_length=500)

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }