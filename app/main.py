from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import uvicorn

from api.routes.events import event as event_router

def get_application() -> FastAPI:
    application = FastAPI(
        title="My API",
        description="My API description",
        version="1.0.0",
        docs_url="/docs",  # <--- Add this line
        openapi_url="/openapi.json"  # <--- Add this line
    )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(event_router)

    return application


app = get_application()

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000, reload=True)