from dataclasses import dataclass

from pydantic import BaseModel


@dataclass
class User(BaseModel):
    user_id: str
    user_password: str
    user_name: str
