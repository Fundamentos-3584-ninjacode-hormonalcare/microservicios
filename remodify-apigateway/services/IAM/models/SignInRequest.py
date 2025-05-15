from pydantic import BaseModel, Field, EmailStr

class SignInRequest(BaseModel):
    username: str = Field(..., min_length=1)
    password: str = Field(..., min_length=8)