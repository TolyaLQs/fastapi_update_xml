# routers/files.py
from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
import os

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return {"filename": file.filename, "size": os.path.getsize(file_path)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


