FastAPI Demo
============

Small FastAPI application that demonstrates a layered structure (routers, services, schemas, utils) and centralised config/logging. Use it as a starter template or learning aid.

Requirements
------------
- Python 3.14+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

Setup
-----
1. **Install dependencies**
   - With uv: `uv sync`
   - Or with pip: `pip install -e .`
2. **Configure environment**
   - Create a `.env` file at the repo root and add required settings, e.g.:
     ```
     API_KEY=replace-me
     APP_NAME=FastAPI Demo
     ENVIRONMENT=dev
     LOG_LEVEL=INFO
     ```
   - Any value missing from `.env` falls back to the defaults in `src/core/config.py`, but `API_KEY` is required.
3. **Run the app**
   ```
   uv run uvicorn src.main:app --reload
   ```
   The service listens on `http://127.0.0.1:8000`. Interactive docs are under `/docs` and `/redoc`.

Example requests
----------------
### Health check
```
GET /health
→ 200 OK
{
  "status": "ok",
  "env": "dev"
}
```

### Create a user
```
POST /users
Content-Type: application/json
{
  "email": "alice@example.com",
  "name": "Alice Doe"
}
→ 201 Created
{
  "id": "9c0b0f41-c5b8-47f9-9ef4-fab956ff62db",
  "email": "alice@example.com",
  "name": "Alice Doe",
  "created_at": "2025-01-01T12:34:56.000000+00:00"
}
```

Project structure
-----------------
- `src/main.py` – FastAPI application factory, router registration, `/health`
- `src/routers/` – HTTP-endpoint definitions (`/users`)
- `src/services/` – business logic (user creation placeholder)
- `src/schemas/` – Pydantic request/response models
- `src/utils/` – helper utilities used by services/routers
- `src/core/` – configuration and logging helpers

Next steps
----------
- Add persistence (database or external API) to `UserService`.
- Expand routers/services for more domains (orders, auth, etc.).
- Wire CI/CD or containerisation if you plan to deploy.
