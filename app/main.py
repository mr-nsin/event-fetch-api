from fastapi import FastAPI, HTTPException
from fastapi.openapi.utils import get_openapi
from app.api.endpoints import events
from app.exceptions import CustomHTTPException
from app.db.base import Base, engine
from typing import List
from datetime import datetime

# Create FastAPI app instance
app = FastAPI()

# Include event endpoints
app.include_router(events.router)

# Run migrations on startup

# Custom exception handler
@app.exception_handler(CustomHTTPException)
async def custom_http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.message}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
