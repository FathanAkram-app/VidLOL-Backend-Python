from typing import Optional

from fastapi import FastAPI
from Models.video_model import Video
from db import Database

app = FastAPI()

db = Database.connectDB()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None, i: Optional[int] = None):
    return {"item_id": item_id, "q": q, "i" : i}

@app.get("/videos/recommended")
def get_videos():
    
    return

@app.post("/videos/upload")
def get_videos(video: Video):
    result = db.videos.insert_one({
        'Title': video.title,
        'Thumbnail':video.thumbnail,
        'Video': video.video,
        'Description': video.description
    })
    print(video.validate)
    print(result)
    return {"status": 200, "message": "Success"}