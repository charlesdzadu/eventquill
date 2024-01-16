from fastapi import APIRouter


router = APIRouter(
    tags=['Users'],
    prefix='/users',
)


@router.get('/me')
def get_authenticated_user():
    return {"message": "Hello World"}
