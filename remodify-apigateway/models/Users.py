from pydantic import BaseModel, Field, EmailStr

class UsersResource(BaseModel):
    email: EmailStr
    description: str = Field(..., min_length=1)
    phone: str = Field(..., min_length=1)
    image: str = Field(..., min_length=1)