from dataclasses import dataclass

from pydantic import BaseModel


@dataclass
class User(BaseModel):
    user_password: str
    user_name: str
    email: str
    disabled: bool = True
