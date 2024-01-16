from fastapi import APIRouter, HTTPException, status


from firebase_admin import auth, exceptions
from app.auth.firebase_authentication import app


from .models import CreatUserAccount


router = APIRouter(
    tags=['Users'],
    prefix='/users',
)


@router.get('/me')
def get_authenticated_user():
    return {"message": "Hello World"}


@router.post('/create-account')
async def create_new_user_account(new_user: CreatUserAccount):
    """ Create a new user account
    """
    try:
        auth.create_user(
            email=new_user.email,
            email_verified=False,
            password=new_user.password,
            display_name=f'{new_user.first_name} {new_user.last_name}',
            disabled=False
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot create user account. Please try again later. ",
        )

    return {"message": "Hello World"}
