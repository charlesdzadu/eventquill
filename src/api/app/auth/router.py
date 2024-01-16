from fastapi import APIRouter

from firebase_admin import auth
from .firebase_authentication import app


router = APIRouter(
    tags=['Auth'],
    prefix='/auth',
)


@router.get('/token')
def get_id_token():
    auth.create_custom_token('some-uid')
    return {"message": "Hello World"}
