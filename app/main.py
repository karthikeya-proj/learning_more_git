from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="Simple Backend API")


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat()
    }
