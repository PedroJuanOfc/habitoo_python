from fastapi import FastAPI

app = FastAPI(title="Habitoo API", version="0.1.0")

@app.get("/health", tags=["infra"])
def health():
    return {"status": "ok"}
