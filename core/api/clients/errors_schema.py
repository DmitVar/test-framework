from typing import Any

from pydantic import BaseModel, Field, ConfigDict


class ValidationErrorSchema(BaseModel):
    """
    A model describing the structure of an API validation error.
    """
    model_config = ConfigDict(populate_by_name=True)

    type: str
    input: Any
    message: str = Field(alias="msg")
    location: str = Field(alias="loc")

class ValidationErrorResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    detail: list[ValidationErrorSchema] = Field(alias="detail")

class InternalErrorResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    
    detail: str = Field(alias="detail")