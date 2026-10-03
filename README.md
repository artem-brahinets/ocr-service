# OCR Service

**v 0.2**

Simple FastAPI service for extracting text from images using OpenCV and Tesseract OCR.

Created for practicing backend and DevOps skills.

## Stack

* Python 3.14
* FastAPI
* OpenCV
* Tesseract OCR
* Pytest
* Docker

## API

### `POST /ocr`

Accepts an image and returns recognized text.

### `GET /health`

Health check endpoint.

## Tests

Run tests locally:

```bash
python -m pytest
```

## Docker

Build the image:

```bash
docker build -t ocr-service:v0.2 .
```

Run the container:

```bash
docker run --rm -p 8000:8000 ocr-service:v0.2
```

The service will be available at:

```text
http://localhost:8000
```

Health check:

```bash
curl http://localhost:8000/health
```

## Version History

### v0.2

* Added Docker support
* Added Dockerfile
* Added `.dockerignore`
* Added `opencv-python-headless` for containerized environment
* OCR service runs inside a Docker container

### v0.1

* Initial FastAPI OCR service
* OpenCV image preprocessing
* Tesseract OCR
* Unit and integration tests

