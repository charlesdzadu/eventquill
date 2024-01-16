from fastapi import APIRouter

router = APIRouter(
    prefix='/attendees',
    tags=['Attendees'],
)


@router.get('/{attendee_id}/')
def get_single_attendee(attendee_id: str):
    pass


@router.put('/{attendee_id}/')
def update_attendee(attendee_id: str):
    pass


@router.delete('/{attendee_id}/')
def delete_attendee(attendee_id: str):
    pass
