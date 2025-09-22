from fastapi import FastAPI

from app.auth.routes import router as auth_router

app = FastAPI(title="Habitoo API", version="0.1.0")

@app.get("/health", tags=["infra"])
def health():
    return {"status": "ok"}

app.include_router(auth_router, prefix="/auth", tags=["auth"])
