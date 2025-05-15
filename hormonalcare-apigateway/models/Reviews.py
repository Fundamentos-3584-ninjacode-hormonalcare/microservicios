from pydantic import BaseModel, Field

class ReviewsResource(BaseModel):
    contractorId: int = Field(..., gt=0)
    projectId: int = Field(..., gt=0)
    duration: str = Field(..., min_length=1)
    rating: int = Field(..., ge=1, le=5)
    comment: str = Field(..., min_length=1)
    image: str = Field(..., min_length=1)

class UpdateReviewResource(BaseModel):
    duration: str = Field(..., min_length=1)
    comment: str = Field(..., min_length=1)
    image: str = Field(..., min_length=1)