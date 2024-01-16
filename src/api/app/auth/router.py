from fastapi import APIRouter


router = APIRouter(
    tags=['Auth'],
    prefix='/auth',
)


@router.get('/check')
def check_for_authentication():
    return {"message": "Hello World"}
