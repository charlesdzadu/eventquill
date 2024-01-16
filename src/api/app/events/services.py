from .models import Event

from app.core.database import app_db


class EventService():
    """ Event Service Class for handling all event related operations"""
    event: Event

    def __init__(self, event: Event):
        self.event = event

    def create_new(self) -> Event:
        """ Create new event """
        data = self.event.model_dump(by_alias=True, exclude=["id"])
        result = app_db.events.insert_one(data)

        res = app_db.events.find_one({"_id": result.inserted_id})
        new_event = Event(**res)

        return new_event
