# routers/files.py
from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
import os
import xml.etree.ElementTree as ET

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            parser = ET.XMLParser(encoding="utf-8")
            tree = ET.parse(source=file_path, parser=parser)
            root = tree.getroot()
            print(root)
            buffer.close()
        otvet = update_file(root)
        return {"filename": file.filename, "size": os.path.getsize(file_path)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


