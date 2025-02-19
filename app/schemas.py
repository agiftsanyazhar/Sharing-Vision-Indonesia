# schemas
from pydantic import BaseModel, Field, ValidationError


def validate_request(data, schema):
    try:
        return schema(**data)
    except ValidationError as e:
        return {"error": e.errors()}


class PostSchema(BaseModel):
    title: str = Field(..., min_length=5, max_length=255)
    content: str = Field(..., min_length=5)
    category: str = Field(..., pattern="^(News|Article|Event|Tips|Other)$")
    status: str = Field(..., pattern="^(Publish|Draft|Trash)$")
