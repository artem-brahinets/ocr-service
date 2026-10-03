from fastapi import FastAPI
from fastapi import UploadFile, File
from app.services import ocr_service
import uvicorn

app = FastAPI()


@app.post("/ocr")
async def ocr(image: UploadFile = File(...)):
    image_bytes = await image.read()
    text_from_img = ocr_service.ocr_img(image_bytes)
    return {"text_from_img": text_from_img}


@app.get("/health")
async def health():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
