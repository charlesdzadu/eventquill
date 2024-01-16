from pydantic import BaseModel, constr
from app.core.custom_base_model import CustomBaseModel


class CreateEvent(BaseModel):
    """ Create Event Model """
    title: constr(min_length=3, max_length=150)
    summary: constr(min_length=3, max_length=500)
    description: constr(min_length=3, max_length=1000)


class Event(CustomBaseModel, CreateEvent):
    """ Event base Model """
