from dataclasses import dataclass

from pydantic import BaseModel


@dataclass
class Post(BaseModel):
    id: int
    writer_id: int
    content: str
    like_num: int


class CreatePost(BaseModel):
    content: str
    like_num: int = 0
    writer_id: int


@dataclass
class Comment(BaseModel):
    content: str
    post_id: int
    user_id: int
