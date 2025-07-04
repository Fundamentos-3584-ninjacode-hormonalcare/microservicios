from pydantic import BaseModel

class SignUpRequest(BaseModel):
    username: str
    password: str
    roles: list[str]
