from pydantic import BaseModel, Field

class RemodelersResource(BaseModel):
    description: str = Field(..., min_length=1)
    phone: str = Field(..., min_length=1)
    subscription: str = Field(..., min_length=1)