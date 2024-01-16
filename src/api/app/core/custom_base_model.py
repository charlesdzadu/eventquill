from pydantic import BaseModel, Field, functional_validators, ConfigDict
from datetime import datetime

from typing import Annotated, Optional


PyObjectId = Annotated[str, functional_validators.BeforeValidator(str)]


class CustomBaseModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    created_at:  datetime = Field(default_factory=datetime.utcnow)
    updated_at:  datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(
        populate_by_name=True,
        by_alias=True,
        arbitrary_types_allowed=True,
    )
