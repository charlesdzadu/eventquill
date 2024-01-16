from fastapi import Security, HTTPException, status, Depends
from fastapi.security.api_key import APIKeyHeader

from app.core.config import envSettings


api_key_scheme = APIKeyHeader(name="X-API-Key", auto_error=False)
master_api_key_scheme = APIKeyHeader(name="X-Master-API-Key", auto_error=False)


def get_api_key_header(api_key: str = Security(api_key_scheme)):
    if api_key == envSettings.MASTER_ACCESS_KEY:
        return api_key
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )


def get_master_api_key_header(api_key: str = Security(master_api_key_scheme)):
    if api_key == envSettings.MASTER_ACCESS_KEY:
        return api_key
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials as master",
        )


master_api_key_dependency = Depends(get_master_api_key_header)
api_key_dependency = Depends(get_api_key_header)
