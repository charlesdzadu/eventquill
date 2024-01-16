from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer

import firebase_admin
from firebase_admin import credentials, auth

from app.core.config import envSettings


credential = credentials.Certificate(envSettings.FIREBASE_ADMIN_SDK_PATH)
app = firebase_admin.initialize_app(credential)

OAUTH_SCHEME = HTTPBearer()


def verify_token(token: str):
    """ Verify the token and return the decoded token if successful. """
    try:
        decoded_token = auth.verify_session_cookie(
            token, check_revoked=True, app=app,)
        uid = decoded_token['uid']
        return uid
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Cannot authenticate user with provided token. Please login again.",
        )


def get_current_user(token: dict = Depends(OAUTH_SCHEME)):
    """ Get the current user from the token. """
    uid = verify_token(token)
    user = auth.get_user(uid, app=app)
    return user
