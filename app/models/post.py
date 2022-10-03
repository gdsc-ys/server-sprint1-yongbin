from dataclasses import dataclass

from pydantic import BaseModel


@dataclass
class Post(BaseModel):
    writer_id: int
    content: str
    like_num: int
