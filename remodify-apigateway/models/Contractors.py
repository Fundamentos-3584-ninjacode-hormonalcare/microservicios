from pydantic import BaseModel, Field

class ContractorsResource(BaseModel):
    description: str = Field(..., min_length=1)
    phone: str = Field(..., min_length=1)