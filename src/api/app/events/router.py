from fastapi import APIRouter

from app.core.database import client

router = APIRouter(
    tags=['Events'],
    prefix='/events',
)


@router.post('/')
def create_new_event():
    db_names = client.list_database_names()

    for db in db_names:
        print(db)
    pass


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
