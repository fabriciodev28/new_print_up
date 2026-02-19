from fastapi import APIRouter, File, UploadFile

router = APIRouter(prefix="/api/upload")

@router.post("/")
async def upload(file: UploadFile = File(...)):
    return {"fileId": file.filename}

@router.post("/estimate")
def estimate(data: dict):
    return {"price": 120.0}
