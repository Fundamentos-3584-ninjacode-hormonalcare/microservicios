from pydantic import BaseModel, Field, EmailStr

class SignUpRequest(BaseModel): 
    username: str = Field(..., min_length=1, max_length=50)
    password: str = Field(..., min_length=8, max_length=120)
    roles: list[str] = Field(default=["ROLE_REMODELER", "ROLE_CONTRACTOR"])
    email: EmailStr
    firstName: str = Field(..., min_length=1)
    paternalSurname: str = Field(..., min_length=1)
    maternalSurname: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    phone: str = Field(..., min_length=1)
    image: str = Field(..., min_length=1)