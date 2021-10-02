from typing import Optional
from pydantic import BaseModel

class Video(BaseModel):
    title: str
    thumbnail: str
    video: str
    description: Optional[str]