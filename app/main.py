from contextlib import asynccontextmanager

import uvicorn
from fastapi import Depends, FastAPI, File, UploadFile
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.init_db import init_db
from app.services import ocr_service
from app.services.ocr_request_service import get_ocr_request, save_ocr_request


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/ocr")
async def ocr(image: UploadFile = File(...),
              db: Session = Depends(get_db)):
    image_bytes = await image.read()
    image_hash = ocr_service.hash_image(image_bytes)

    ocr_request = get_ocr_request(db, image_hash)

    if ocr_request is not None:
        text_from_img = ocr_request.recognized_text
    else:
        text_from_img = ocr_service.ocr_img(image_bytes)
        save_ocr_request(db, image_hash, text_from_img)

    return {"text_from_img": text_from_img}


@app.get("/health")
async def health():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
