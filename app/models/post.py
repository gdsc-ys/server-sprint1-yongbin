from dataclasses import dataclass

from pydantic import BaseModel


@dataclass
class Post(BaseModel):
    writer_id: int
    content: str
    like_num: int


@dataclass
class Comment(BaseModel):
    content: str
    post_id: int
    user_id : int
