from fastapi import APIRouter
from bson import ObjectId

from app.core.database import client
from .models import Event, CreateEvent
from .services import EventService

router = APIRouter(
    tags=['Events'],
    prefix='/events',
)


@router.post('/', response_model=Event)
def create_new_event(event: CreateEvent):
    """ Create new event """
    event = Event(**event.model_dump())
    event_service = EventService(event)
    new_event = event_service.create_new()

    return new_event


@router.get('/')
def get_user_all_events(uid: str):
    pass


@router.get('/{event_id}')
def get_event(event_id: str):
    pass


@router.put('/{event_id}')
def update_event(event_id: str):
    pass


@router.delete('/{event_id}')
def delete_event(event_id: str):
    pass


@router.get('/{event_id}/attendees')
def get_event_attendees(event_id: str):
    pass
