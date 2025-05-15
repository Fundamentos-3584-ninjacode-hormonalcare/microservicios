from pydantic import BaseModel, Field, validator

class BusinessResource(BaseModel):
    name: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    address: str = Field(..., min_length=1)
    city: str = Field(..., min_length=1)
    image: str = Field(..., min_length=1)
    expertise: str = Field(..., min_length=1)
    remodelerId: int = Field(..., gt=0)

    @validator('image')
    def validate_image(cls, v):
        if not v.startswith('http'):
            raise ValueError('Image URL must start with http')
        return v