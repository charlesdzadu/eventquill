from datetime import datetime
from pydantic import BaseModel, constr, EmailStr, Field


from app.core.custom_base_model import CustomBaseModel


class CreatUserAccount(BaseModel):
    first_name: constr(min_length=3, max_length=50) = Field(...,
                                                            description='First name of the user.')
    last_name: constr(min_length=3, max_length=50) = Field(...,
                                                           description='Last name of the user.')
    password: constr(min_length=8, max_length=100) = Field(...,
                                                           description='Password of the user.')
    email: EmailStr = Field(..., description='Email of the user.')


class User(CustomBaseModel):
    """ User base Model """
    first_name: str = Field(..., description='First name of the user.')
    last_name: str = Field(..., description='Last name of the user.')
    email: EmailStr = Field(..., description='Email of the user.')
    is_active: bool = Field(..., description='Is user active.')
    is_verified: bool = Field(..., description='Is user verified.')

    class Config:
        from_attributes = True
