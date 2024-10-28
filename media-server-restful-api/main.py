import asyncio
import os
import time
import utils

from typing import Annotated
from fastapi import FastAPI, File, UploadFile, HTTPException

app = FastAPI()

# Define allowed MIME types and file extensions for videos
ALLOWED_FILE_TYPES = [
    # Video Types
    'video/mp4', 'video/x-matroska', 'video/x-msvideo', 'video/quicktime',
    'video/x-ms-wmv', 'video/x-flv', 'video/webm', 'video/x-m4v',
    'video/3gpp', 'video/ogg', 'video/mp2t', 'video/mpeg',
    # Audio Types
    'audio/mpeg', 'audio/wav', 'audio/aac', 'audio/ogg', 'audio/flac',
    'audio/mp4', 'audio/x-ms-wma', 'audio/opus', 'audio/aiff', 'audio/midi',
    'audio/webm'
]

ALLOWED_FILE_EXTENSIONS = [
    # Video Extensions
    '.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm', '.m4v',
    '.3gp', '.ogv', '.ts', '.mpeg',
    # Audio Extensions
    '.mp3', '.wav', '.aac', '.ogg', '.flac', '.m4a', '.wma', '.opus', '.aiff', 
    '.mid', '.weba'
]

@app.get("/")
def home():
    return {"message": "Visit the endpoint: /api/v1/extract_text to perform OCR."}

@app.post("/upload/")
async def upload_file(
    file: Annotated[UploadFile, File(description="A file read as UploadFile")],
):
    # Check content type
    if file.content_type not in ALLOWED_FILE_TYPES:
        raise HTTPException(status_code=400, detail="Invalid file type")

    # Check file extension
    _, ext = os.path.splitext(file.filename)
    if ext.lower() not in ALLOWED_FILE_EXTENSIONS:
        raise HTTPException(status_code=400, detail=f"Invalid file extension: {ext}")

    temp_file = utils._save_file_to_server(file)
    
    return {
        "file": temp_file
    }

@app.post("/playback/")
async def playback_file(filename: str = "video1.mp4"):
    utils._playback_via_vlc(filename)
    return {
        "message": f"Playing {filename} in VLC",
        "gogo": ""
    }
