from pydantic import BaseModel, Field, EmailStr

class ProfilesResource(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)
    typeUser: str = Field(..., min_length=1)
    firstName: str = Field(..., min_length=1)
    paternalSurname: str = Field(..., min_length=1)
    maternalSurname: str = Field(..., min_length=1)