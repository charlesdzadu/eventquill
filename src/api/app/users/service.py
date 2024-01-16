from .models import User


class UserService():
    def __init__(self, user: User):
        self.user = user
