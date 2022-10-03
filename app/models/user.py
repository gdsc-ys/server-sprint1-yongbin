from pydantic import BaseModel


class User(BaseModel):
    user_id: str
    user_password: str
    user_name: str
