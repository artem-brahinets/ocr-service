# OCR Service

**v0.3**

A simple FastAPI service for extracting text from images using OpenCV and Tesseract OCR.

Created for practicing backend development and DevOps skills.

## Stack

- Python 3.14
- FastAPI
- OpenCV
- Tesseract OCR
- PostgreSQL 16
- SQLAlchemy
- Psycopg 3
- Pytest
- Docker
- Docker Compose

## Features

- Text extraction from images
- Image preprocessing with OpenCV
- English OCR support
- PostgreSQL integration
- OCR result persistence
- Result caching using SHA-256 image hashes
- Automated tests

## API

### `POST /ocr`

Accepts an image and returns recognized text.

If the same image has already been processed, the service returns the cached result instead of running OCR again.

### `GET /health`

Health check endpoint.

Example response:

```json
{
  "status": "ok"
}
```

## Docker Compose

### 1. Configure environment variables

Create a `.env` file in the project root using `.env.example` as a template.

Configure the PostgreSQL credentials and database name.

### 2. Build and start the services

```bash
docker compose up -d --build
```

This starts:

- `ocr-service` - FastAPI application
- `db` - PostgreSQL database

### 3. Check running containers

```bash
docker compose ps
```

### 4. Run tests

```bash
docker compose exec ocr-service python -m pytest -v
```

## Access

The API will be available at:

```text
http://localhost:8000
```

Interactive API documentation:

```text
http://localhost:8000/docs
```

Health check:

```bash
curl http://localhost:8000/health
```

## Database

PostgreSQL stores OCR request results.

Each image is identified by its SHA-256 hash.

When an image is submitted:

1. The service calculates its SHA-256 hash.
2. It checks whether the result already exists in PostgreSQL.
3. If a cached result exists, it returns the stored text.
4. Otherwise, it runs OCR and saves the result in the database.

PostgreSQL data is persisted using a Docker named volume.

## Version History

### v0.3

- Added PostgreSQL integration
- Added SQLAlchemy ORM
- Added OCR request persistence
- Added SHA-256 image hashing
- Implemented OCR result caching
- Added Docker Compose configuration for PostgreSQL
- Updated tests to run inside Docker

### v0.2

- Added Docker support
- Added Dockerfile
- Added `.dockerignore`
- Added `opencv-python-headless` for containerized environment
- OCR service runs inside a Docker container

### v0.1

- Initial FastAPI OCR service
- OpenCV image preprocessing
- Tesseract OCR
- Unit and integration tests

